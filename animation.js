
// animation.js
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('hero-animation');
    if (!container) return;

    // SCENE
    const scene = new THREE.Scene();
    // scene.fog = new THREE.FogExp2(0x000000, 0.002); // Optional fog

    // CAMERA
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.z = 1.8; // Zoom level

    // RENDERER
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // GEOMETRY
    // Increased detail level to 3 (or 4) for smoother/more polygons
    // IcosahedronGeometry(radius, detail) - detail > 1 makes it rounder
    const geometry = new THREE.IcosahedronGeometry(1.2, 4);

    // MATERIAL
    const material = new THREE.MeshBasicMaterial({
        color: 0xffea00, // Brighter Vivid Yellow
        wireframe: true,
        transparent: true,
        opacity: 0.8, // High opacity for brightness
        wireframeLinewidth: 2, // Thicker lines
    });

    // MESH
    const sphere = new THREE.Mesh(geometry, material);
    sphere.position.x = -2;
    scene.add(sphere);

    // REMOVED SECONDARY SPHERE to fix the "two globes" look
    // If you want a subtle glow effect instead, usage of shaders or post-processing would be better,
    // but for now, a single high-poly wireframe is cleanest.


    // ANIMATION LOOP
    function animate() {
        requestAnimationFrame(animate);

        sphere.rotation.y += 0.002;
        sphere.rotation.x += 0.001;

        sphere.rotation.y += 0.002;
        sphere.rotation.x += 0.001;

        renderer.render(scene, camera);
    }
    animate();

    // RESIZE HANDLE
    window.addEventListener('resize', () => {
        const width = container.clientWidth;
        const height = container.clientHeight;

        camera.aspect = width / height;
        camera.updateProjectionMatrix();

        renderer.setSize(width, height);
    });
});
