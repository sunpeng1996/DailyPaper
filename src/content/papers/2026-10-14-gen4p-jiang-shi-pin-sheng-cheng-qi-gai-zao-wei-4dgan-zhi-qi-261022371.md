---
title: 'Gen4P: Video Generators are 4D Perceivers'
title_zh: Gen4P：将视频生成器改造为4D感知器
authors:
- Yitong Xia
- Zeren Jiang
- Chuanxia Zheng
affiliations:
- Nanyang Technological University
- University of Oxford
arxiv_id: '2610.22371'
url: https://arxiv.org/abs/2610.22371
pdf_url: https://arxiv.org/pdf/2610.22371
published: '2026-10-14'
collected: '2026-10-17'
category: Multimodal
direction: 多模态视频4D感知框架设计
tags:
- Video Generation
- 4D Perception
- LoRA
- Cross-Attention
- Monocular Video
one_liner: 将预训练视频生成器改造为无迭代降噪的前馈4D感知框架，实现单目视频多4D属性SOTA预测
practical_value: '- 可借鉴预训练生成模型复用为感知任务的范式，将短视频生成大模型改造为商品3D结构/动态动作感知工具，支撑短视频商品理解、AR试穿等场景

  - 可复用冻结预训练LoRA作为领域先验的插件式方案，无需新增训练参数即可为多模态模型注入商品纹理、结构等特定领域知识，降低微调成本

  - 按需查询+连续时间查询的设计可迁移到视频交互Agent，支持用户指定时空维度的视频内容灵活检索、属性抽取与动态跟踪'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有单目视频4D重建需同时捕获场景静态几何结构与动态时序运动，传统方案精度不足，且依赖迭代计算时延高，难以落地实时场景。
### 方法关键点
1. 直接将预训练视频生成器改造为无需迭代降噪的前馈4D感知框架Gen4P，单次编码器pass处理视频隐层，通过轻量交叉注意力解码器输出指定4D属性
2. 设计按需查询机制支持灵活空间采样，配套连续时间查询实现时序维度的灵活调整
3. 插件式引入预训练视频深度LoRA作为冻结几何先验，不新增可训练参数即可显著提升几何感知效果
### 关键结果
在3D点跟踪、视频深度估计、相机位姿估计三类任务上达到SOTA或可比性能，可稳定处理野外复杂运动场景的精细结构跟踪
