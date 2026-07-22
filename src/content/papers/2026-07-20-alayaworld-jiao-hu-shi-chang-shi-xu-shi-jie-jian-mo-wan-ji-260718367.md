---
title: 'AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report'
title_zh: AlayaWorld：交互式长时序世界建模完整技术报告
authors:
- AlayaWorld Team
- Kaipeng Zhang
- Chuanhao Li
- Yifan Zhan
- Yongtao Ge
- Yuanyang Yin
- Jiaming Tan
- Kang He
- Liaoyuan Fan
- Mingliang Zhai
affiliations:
- Alaya Lab
arxiv_id: '2607.18367'
url: https://arxiv.org/abs/2607.18367
pdf_url: https://arxiv.org/pdf/2607.18367
published: '2026-07-20'
collected: '2026-07-22'
category: Other
direction: 交互式长时序视频世界模型构建
tags:
- World_Model
- Video_Diffusion
- Diffusion_Transformer
- Autoregressive_Distillation
- Long_Horizon_Generation
one_liner: 提出15B参数交互式长时序视频世界模型AlayaWorld，仅需4采样步实现24fps高清长视频稳定生成
practical_value: '- 长序列生成漂移抑制方案：训练引入自生成损坏历史+预测残差的策略，可迁移到生成式推荐长用户行为序列建模、多轮对话推荐一致性保持场景

  - 推理加速蒸馏框架：结合分布匹配蒸馏、self-forcing++、一致性蒸馏的离散自回归蒸馏方法，可复用在Diffusion类电商商品图/短视频生成、推荐文案生成的推理提速优化

  - 有限上下文时序记忆设计：持久sink帧+压缩时序历史+几何对齐空间记忆的组合方案，可借鉴到多轮Agent交互状态记忆、长会话推荐上下文管理'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统游戏开发依赖重人力的资产生产、动画、物理、编程管线，视频世界模型可基于文本/图像/视频快速生成可交互虚拟环境，但需同时满足交互性、时空一致性、长时序稳定生成、低延迟响应四大核心要求。
### 方法关键点
1. 底座为15B参数视频Diffusion Transformer，在相机轨迹和可切换text prompt控制下自回归生成短latent chunk；
2. 上下文采用持久sink帧+压缩时序历史+几何对齐空间记忆+最近帧conditioning的组合设计，训练时引入损坏历史和自生成roll-out的预测残差抑制长期漂移；
3. 提出离散自回归蒸馏框架，将每chunk推理采样步从30降至4。
### 关键结果
可生成24fps的540P/720P高清视频，在iWorld-Bench长时序生成任务上性能达SOTA，全栈开源可扩展。
