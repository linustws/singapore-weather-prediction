// import {readFileSync} from 'fs';
// import {resolve} from 'path';
//
// export async function load() {
//     const filePath = resolve('src/lib/model/model_iframe_figures/figure_4.html');
//     const htmlContent = readFileSync(filePath, 'utf-8');
//
//     // console.log(htmlContent)
//
//     // const adjustedHtmlContent = htmlContent.replace(
//     //     /src="(.*?)"/g,
//     //     (match, src) => {
//     //         if (!src.startsWith('http') && !src.startsWith('/')) {
//     //             const relativeSrc =`src/lib/model/${src}`;
//     //             return `src="${relativeSrc}"`;
//     //         }
//     //         return match;
//     //     }
//     // );
//
//     return { htmlContent };
// }
//