---
title: 'Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language
  Mixture-of-Experts'
title_zh: 基于几何引导的视觉语言混合专家模型负载均衡方法ReBA
authors:
- Ziang Wu
- Peng Jin
- Qishen Yin
- Munan Ning
- Hao Li
- Peizhen Zhang
- Li Yuan
affiliations:
- 北京大学深圳研究生院
- 鹏城实验室
- 北京大学软件与微电子学院
- Qwen Team
- 中山大学
arxiv_id: '2608.00574'
url: https://arxiv.org/abs/2608.00574
pdf_url: https://arxiv.org/pdf/2608.00574
published: '2026-07-31'
collected: '2026-08-04'
category: Training
direction: 多模态MoE 负载均衡训练优化
tags:
- MoE
- Load Balancing
- Multimodal LLM
- Vision-Language
- Auxiliary Loss
one_liner: 提出分模态+图像级实例的几何引导负载均衡策略ReBA，解决多模态MoE跨token比例的负载失衡问题
practical_value: '- 多模态MoE部署场景直接复用分模态均衡思路：针对电商图文搜索、多模态商品推荐场景的请求图文比例动态波动问题，拆分模态独立的负载均衡损失，避免单模态负载失衡被混合统计掩盖，降低推理阶段的专家拖尾延迟

  - 高相关token组的均衡优化技巧可迁移：对商品图拆分的多patch、长用户行为序列这类内部高相关性的token组，采用组内路由平均、组间等权的统计方式计算均衡损失，避免长序列/多patch样本过度主导路由优化方向

  - 多模态MoE上线评估可参考波动测试框架：不要仅在固定token配比下测负载，需覆盖业务真实的图文比例、图像分辨率分布，评估平均负载和最坏场景负载，避免上线后因请求分布变化出现性能骤降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态MoE采用的标准Switch辅助损失（Std-Aux）仅在混合token维度做负载均衡，训练阶段仅能在固定图文token配比下达到均衡；当推理阶段请求的图文比例、图像分辨率/分块数动态变化时，图像和文本各自的负载失衡会因误差方向相反在混合统计中抵消，导致同一路由器的负载失衡程度波动可达5倍以上，严重削弱MoE的稀疏计算收益。

### 方法关键点
- 先验观测到多模态路由的两层几何边界：①图像和文本token在路由输入空间完全分区，线性路由器可轻易将两类token路由到不同专家，形成模态互补的负载误差；②同一张图的patch token路由相关性远高于跨图token，单图可作为独立路由单元。
- 提出ReBA负载均衡损失：拆分独立的图像、文本模态均衡项，从根源避免跨模态负载误差抵消，要求两类模态各自达到负载均衡。
- 图像维度以单图为路由实例：单图内所有token的路由概率平均后，再对所有图像做等权均衡，避免高分辨率多patch图的token数更多、过度影响路由优化方向；文本侧保留全局池化即可。

### 关键实验
在Split-Qwen3VL-4B、Split-InternVL3-8B等4个多模态拆分MoE骨干上测试，对比Std-Aux基线：所有benchmark的平均层CV（负载均衡指标）下降60%以上，平均任务精度与基线持平；跨图文token比例波动场景下，负载曲线曲率降低96.3%，最坏场景RMS-CV下降超67%；理想专家并行计算效率提升1.23-1.25倍。

**最值得记住的一句话**：多模态MoE的负载均衡不能仅看混合统计值，需基于输入的模态、样本结构设计分层均衡目标，才能适配真实请求的分布波动。
