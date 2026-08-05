---
title: 'JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion'
title_zh: JoyAI-Video-Edit：基于自回归扩散的实时开放式视频编辑框架
authors:
- Yicheng Xiao
- Wenxun Dai
- Xinran Qin
- Lin Song
- Maoquan Zhang
- Hang Xu
- Yukang Chen
- Yitong Li
- Guohui Zhang
- Yuan Zhang
affiliations:
- Joy Future Academy, JD
arxiv_id: '2608.03974'
url: https://arxiv.org/abs/2608.03974
pdf_url: https://arxiv.org/pdf/2608.03974
published: '2026-08-03'
collected: '2026-08-05'
category: Multimodal
direction: 多模态生成 · 实时流视频编辑
tags:
- Autoregressive Diffusion
- Video Editing
- Real-time Generation
- Knowledge Distillation
- KV Cache
one_liner: 16B参数自回归扩散视频编辑框架，单B200 GPU实现720p 30FPS实时流编辑，效果媲美离线SOTA
practical_value: '- 电商直播实时特效、商品短视频批量风格化场景可直接复用分块自回归+滑动窗口KV cache架构，实现无限流长视频的流式处理，内存占用不随视频长度增长

  - SA-DMD蒸馏trick可迁移到生成式推荐的文案/图像生成任务，在少步加速生成时同时保证指令遵循度和原始信息保真，减少生成漂移

  - 长序列自回归训练的分段优化+动态镜像循环策略，可适配用户长行为序列建模、长视频生成推荐等场景，解决长序列训练OOM和误差累积问题

  - FP8量化、算子融合、计算图预编译的工程优化方案，可直接复用在大模型生成类服务的低延迟部署，提升吞吐降低延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有高画质视频编辑多为离线方案，依赖未来帧全局计算，无法适配直播、实时内容创作等流输入场景；现有流编辑方案存在训练推理分布不匹配、源内容漂移、长序列误差累积、延迟高画质差等问题，无法满足实时编辑的低延迟、高保真、长时一致性要求。
### 方法关键点
- 架构：16B参数自回归扩散框架，包含MLLM条件编码器、因果视频VAE、多模态扩散Transformer，支持指令引导和参考图引导两类视频编辑任务
- 分块自回归适配：块内双向注意力、块间因果注意力，滑动窗口保留最近块+首块全局锚点，控制内存占用；引入重采样强迫缩小训练推理分布差
- SA-DMD蒸馏：在DMD基础上增加源内容锚定的双轴引导项，将多步扩散蒸馏为2步生成，同时兼顾编辑一致性和源内容保真度
- 长时自回归蒸馏：长序列分段优化+动态镜像循环策略，解决长序列训练OOM和误差累积问题
- 工程优化：FP8量化、KV cache复用、算子融合、计算图编译大幅降低推理延迟
### 关键结果
- OpenVE-Bench短视频基准：整体得分3.60，领先现有流编辑方案0.98~2.37分，效果媲美离线SOTA系统
- 自研LongV2VBench长视频基准：整体得分3.30，领先次优流编辑方案1.59分，全类别任务排名第一
- 部署性能：单Nvidia B200 GPU实现720p 30.19FPS端到端编辑，请求响应延迟仅226ms
### 核心结论
流生成任务的核心是在低延迟约束下平衡历史连贯性、指令遵循度、源内容保真度三者的关系，针对性的蒸馏和训练优化可大幅缩小流方案与离线方案的质量差距
