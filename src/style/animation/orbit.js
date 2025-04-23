// CONFIGURE ORBIT ANIMATION AND TOOLTIP

document.addEventListener("DOMContentLoaded", () => {
  const icons = Array.from(document.querySelectorAll(".orbit-circle"));
  const orbitCenter = document.getElementById("orbit-center");

  // Orbit definition (angle start, radius)
  const orbitData = [
    { angle: 15, radius: 110 },
    { angle: 255, radius: 110 },
    { angle: 112, radius: 170 },
    { angle: 330, radius: 170 },
    { angle: 150, radius: 230 },
    { angle: 205, radius: 230 },
    { angle: 42, radius: 230 },
  ];

  let t0 = Date.now();
  function animate() {
    // How many degrees per second
    const SPEED = 9; // deg/sec: slow and smooth
    const t = (Date.now() - t0) / 1000;
    icons.forEach((icon, i) => {
      const { angle, radius } = orbitData[i % orbitData.length];
      const theta = (((angle + t * SPEED) % 360) * Math.PI) / 180;
      // 260, 260 is center (SVG coordinates)
      const cx = 260 + Math.cos(theta) * radius;
      const cy = 260 + Math.sin(theta) * radius;
      icon.style.left = `${cx}px`;
      icon.style.top = `${cy}px`;
    });
    requestAnimationFrame(animate);
  }
  animate();

  // Tooltip is handled by CSS (hover). You can add touch/mouseover support here if needed.
});
