---
title: 'HuRo: Robotizing Human Videos for Scalable VLA Pretraining'
title_zh: HuRo：将人类视频机器人化用于可扩展VLA预训练
authors:
- Jinho Jeong
- Se June Joo
- Jaehyun Kang
- Dongyun Kim
- Yena Kim
- Hanjung Kim
- Seon Joo Kim
affiliations:
- RLWRLD
- Yonsei University
arxiv_id: '2609.10706'
url: https://arxiv.org/abs/2609.10706
pdf_url: https://arxiv.org/pdf/2609.10706
published: '2026-09-17'
collected: '2026-09-22'
category: Multimodal
direction: 多模态VLA预训练 · 跨域数据对齐
tags:
- VLA Pretraining
- Multimodal Alignment
- Data Generation
- Cross-domain Transfer
- Dataset Construction
one_liner: 提出人类视频机器人化流水线，构建630K样本HuRo数据集提升VLA预训练效果
practical_value: '- 跨模态跨域数据对齐的流水线设计思路，可迁移到电商多模态推荐预训练，比如将异构UGC内容转换为推荐系统可直接使用的对齐样本

  - 用易获取的低标注成本数据补全稀缺高价值业务数据的范式，可复用在广告/推荐小样本场景，降低数据采集成本

  - 端到端带动作/行为对齐的预训练效果优于纯特征迁移的结论，可指导多模态交互Agent的预训练数据构造策略'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA预训练依赖的真实机器人交互数据采集成本极高，人类视频数据量丰富、覆盖场景广，但人与机器人的具身gap导致无法直接复用，现有对齐方案无法规模化落地。
### 方法关键点
- 端到端机器人化流水线可将异构人类视频转换为机器人对齐的观测、动作轨迹，同时补全不同标注层级缺失的中间信号
- 基于流水线构建HuRo数据集，包含5个人类视频来源的630K机器人化片段、1.42亿处理后帧
### 关键结果
4个真实世界操作任务上，增加机器人化预训练数据后，整体任务完成率从51.5%提升至80.3%，空间/视觉偏移下的OOD完成率从34.9%提升至72.2%；消融验证视觉机器人化可提升OOD鲁棒性，带重定向动作的端到端预训练效果优于纯视觉迁移。
