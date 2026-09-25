---
title: Training Object Permanence in World Models
title_zh: 世界模型的物体恒存性训练
authors:
- Haotian Zhang
- Fengyuan Yu
- Dezhi Luo
- Haoran Sun
- Zehong Zhao
- Qingying Gao
- Yihan Li
- Siyuan An
- Huayi Qin
- Yilan Zhang
affiliations:
- Carnegie Mellon University
- University of Southern California
- University of Michigan
- Johns Hopkins University
- Columbia University
arxiv_id: '2609.28654'
url: https://arxiv.org/abs/2609.28654
pdf_url: https://arxiv.org/pdf/2609.28654
published: '2026-09-22'
collected: '2026-09-25'
category: Training
direction: 世界模型训练 · 认知先验注入
tags:
- World Model
- Object Permanence
- Training Dataset
- Benchmark
- Video Generation
one_liner: 构建面向世界模型物体恒存性的WROP基准数据集，训练的16B PWM-WROP在视频延续任务中登顶
practical_value: '- 做交互式Agent/电商数字人场景时，可参考WROP的认知先验数据集构建思路，给多模态模型注入物理常识，减少交互时的物体逻辑错误

  - 数据生成可复用「固定核心任务结构+随机无关参数」的范式，低门槛生成大量高质量训练样本，适配业务场景的特定能力注入需求

  - pairwise Elo盲测的评估方法可直接迁移到生成式推荐、商品短视频生成的效果评估，比客观指标更贴近用户真实感知'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前视频生成类世界模型已涌现推理能力，是构建类人物理智能的核心载体，但普遍缺失人类认知核心的物体恒存、实体刚性先验，暂无针对性的训练与评估基准。
### 方法关键点
1. 构建WROP数据基础设施，覆盖6类认知任务、150个人工设计的Blender生成器，固定任务核心认知结构的同时随机化光照、相机角度、速度等无关参数，单任务生成超1万样本，总训练语料1.5M，配套300题评测集。
2. 训练16B参数的PWM-WROP世界模型，基于原生PyTorch训练栈在AWS Trainium2上实现。
### 关键结果
在14个不同类型视频模型的盲测 pairwise Elo 排序中，PWM-WROP在视频延续类模型中排名第一，总榜排名第三，仅与前两名参考转视频模型存在统计级性能差距。
