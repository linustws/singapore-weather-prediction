<script>
    import "../app.css";
    import Navbar from "$lib/components/Navbar.svelte";
</script>

<main>
    <Navbar/>

    <div class="slot"><slot/></div>
</main>

<style lang="postcss">
    main {
        height: 100vh;
        width: 100%;
        background-image: url("$lib/images/background.png");
        background-size: cover;
        background-position: center;
        font-size: 1.5rem;
        font-weight: 300;
        position: fixed;
    }

    /*
    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        box-shadow: inset 0 0 10px 10px transparent;
        border: solid 3px transparent;
        margin-top: 52px;
    }

    ::-webkit-scrollbar-thumb {
        box-shadow: inset 0 0 10px 10px rgba(43, 43, 43, 0.75);
        border-radius: 1rem;
        border: solid 3px transparent;
        height: 100px;
    }

    ::-webkit-scrollbar-thumb:hover {
        box-shadow: inset 0 0 10px 10px rgba(43, 43, 43, 0.5);
    }
     */

    .slot {
        margin-top: 52px;
        overflow: auto;
        height: calc(100vh - 52px);
    }
</style>
