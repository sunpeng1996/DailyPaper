---
title: 'SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization'
title_zh: SonoWorld4D：基于扩散同步的单视频转4D视听场景方法
authors:
- Derong Jin
- Xiyi Chen
- Ming C. Lin
- Ruohan Gao
affiliations:
- University of Maryland, College Park
arxiv_id: '2610.40640'
url: https://arxiv.org/abs/2610.40640
pdf_url: https://arxiv.org/pdf/2610.40640
published: '2026-10-29'
collected: '2026-10-31'
category: Multimodal
direction: 多模态生成 · 4D视听场景重建
tags:
- Diffusion Model
- 4D Scene Generation
- Audio-Visual Learning
- Spatial Audio
- Dynamic Reconstruction
one_liner: 提出SonoWorld4D框架，实现单目视频输入生成可探索的时空对齐4D视听场景
practical_value: '- 电商虚拟逛店、3D直播场景可复用双空间扩散同步方法实现多声源空间音频与动态画面对齐，大幅提升沉浸式交互体验

  - 商品动态展示内容生产环节可借鉴单视频输入生成全视角4D场景的技术思路，降低3D内容制作的素材成本

  - AR/VR电商试穿试用场景可参考动静分离的场景重建逻辑，优化实时渲染的性能开销，降低端侧算力要求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有4D动态场景生成技术仅覆盖视觉维度，未建模与动态物体、事件天然耦合的声音信号，无法输出完整可交互的沉浸式场景。

### 方法关键点
1. 定义Video-to-4DAVScene新任务，输入单目视频即可输出可自由探索的时空同步4D视听场景；
2. 采用动静分离架构：生成360°静态背景，重建发声前景物体的显式运动轨迹；
3. 引入双空间音频扩散同步机制，生成符合物理规则的多声源一致性声场，支持实时新视角视觉+空间音频渲染。

### 关键结果
在真实动态场景数据集完成验证，用户研究显示生成的空间音频与场景几何、视觉内容匹配度高，感知真实度符合预期。
