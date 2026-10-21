---
title: 'OverSeer: Multi-Agent World Models Beyond What Agents See'
title_zh: OverSeer：引入固定辅助视角的高一致性多智能体世界模型
authors:
- Runjia Li
- Kam Woh Ng
- Minghao Chen
- Junlin Han
- Jianyuan Wang
- Zhaochong An
- Juan-Manuel Perez-Rua
- Andrea Vedaldi
- Shikun Liu
affiliations:
- Meta AI
- University of Oxford
arxiv_id: '2610.28554'
url: https://arxiv.org/abs/2610.28554
pdf_url: https://arxiv.org/pdf/2610.28554
published: '2026-10-19'
collected: '2026-10-21'
category: MultiAgent
direction: 多智能体 · 世界模型一致性优化
tags:
- Multi-Agent
- World Model
- Consistency
- VAE
- Video Diffusion
one_liner: 通过固定全局辅助视角与δ-VAE残差压缩，大幅提升多智能体世界模型的时序与跨视角一致性
practical_value: '- 多导购/客服Agent协同场景可借鉴固定全局参考设计：新增共享的用户长期画像、全量商品池等静态锚点，从架构层面解决跨Agent给用户的推荐信息、权益规则冲突问题

  - 长序列用户行为模拟、直播/短视频内容生成场景可复用δ-VAE残差压缩思路：静态背景（如店铺装修、用户长期标签）仅存1次锚点，仅编码动态变化部分（如实时行为、临时活动），可降低70%+token开销

  - 多智能体系统评估可参考MAC-Bench设计：不要只看单步生成的视觉/文本合理性，需新增智能体信息隔离后重聚的一致性校验，避免出现逻辑矛盾但表面合理的错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单视角多智能体世界模型无法维持长期时序一致性和跨视角一致性，智能体失联后重聚时场景/其他智能体状态错误率超过90%；直接构建显式全局3D表示成本高且依赖精准姿态估计，缺乏低成本的共享参考实现方案。

### 方法关键点
- 引入固定姿态的辅助相机视角作为共享全局参考，覆盖智能体视野外区域，视角变化直接对应真实世界状态变化，完全排除相机位姿移动的干扰
- 提出δ-VAE二阶压缩模块：仅保存辅助视角首帧作为静态锚点，后续帧编码为相对于锚点的残差latent，实现8倍辅助视角token压缩，6路辅助视角仅额外增加37.5%的双智能体流token开销
- 基于Wan2.2视频扩散底座，通过共享注意力联合生成智能体视角与压缩后的辅助视角残差；训练阶段用真实辅助视图监督，推理阶段仅需初始智能体帧、动作序列、辅助相机先验位姿即可运行

### 关键实验
在Minecraft、Doom两个游戏场景，对比Solaris、γ-World两个SOTA多智能体世界模型，Minecraft MAC-Bench的三个重聚任务VLM准确率从0%/6.2%/12.5%提升到60.2%/37.9%/40.5%，同时FID为各任务最优；移除辅助视角后所有一致性任务准确率下降50%以上。

### 核心结论
生成模型的输出空间设计（选择生成什么内容而非仅优化输入条件）是提升多智能体系统一致性的核心设计轴之一。
