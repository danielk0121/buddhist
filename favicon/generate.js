const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const svgPath = path.join(__dirname, "favicon.svg");
const svgBuffer = fs.readFileSync(svgPath);

const sizes = [
  { name: "favicon-16x16.png", size: 16 },
  { name: "favicon-32x32.png", size: 32 },
  { name: "favicon-192x192.png", size: 192 },
  { name: "favicon-512x512.png", size: 512 },
];

async function generate() {
  for (const { name, size } of sizes) {
    const outPath = path.join(__dirname, name);
    await sharp(svgBuffer)
      .resize(size, size)
      .png()
      .toFile(outPath);
    console.log(`생성: ${name} (${size}x${size})`);
  }

  // favicon.ico — 32x32 PNG를 ICO로 변환
  const icoPath = path.join(__dirname, "favicon.ico");
  await sharp(svgBuffer)
    .resize(32, 32)
    .png()
    .toFile(icoPath.replace(".ico", "_tmp.png"));

  // ICO는 sharp가 직접 지원하지 않으므로 32x32 PNG를 ico로 복사
  fs.copyFileSync(icoPath.replace(".ico", "_tmp.png"), icoPath);
  fs.unlinkSync(icoPath.replace(".ico", "_tmp.png"));
  console.log("생성: favicon.ico (32x32, PNG 포맷 ICO)");

  console.log("\n모든 파비콘 이미지 생성 완료.");
}

generate().catch((err) => {
  console.error("오류:", err);
  process.exit(1);
});
