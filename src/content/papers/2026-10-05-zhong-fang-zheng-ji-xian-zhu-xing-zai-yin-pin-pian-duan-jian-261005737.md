---
title: Revisiting Frame-Wise Saliency for Audio Moment Retrieval
title_zh: 重访帧级显著性在音频片段检索中的应用
authors:
- Tatsuya Komatsu
- Hokuto Munakata
affiliations:
- LY Corporation, Tokyo, Japan
arxiv_id: '2610.05737'
url: https://arxiv.org/abs/2610.05737
pdf_url: https://arxiv.org/pdf/2610.05737
published: '2026-10-05'
collected: '2026-10-11'
category: Other
direction: 音频片段检索 · DETR 帧级显著性优化
tags:
- Audio Moment Retrieval
- DETR
- Frame-wise Saliency
- Sound Event Detection
- CASTELLA
one_liner: 证明DETR类音频片段检索模型的帧级显著性序列可直接替代解码器输出，大幅提升检索效果
practical_value: '- 多任务模型训练阶段的辅助任务输出（如显著性序列），推理阶段可替代主输出，同时降本提效，可迁移到推荐系统多任务排序模型优化

  - 无参数启发式后处理规则可替代带参数的解码器预测，降低推理延迟，适合端侧推荐、轻量Agent场景的部署优化

  - 细粒度短周期检索/匹配场景（如短视频高光片段推荐、广告片段截取），优先用帧级细粒度特征直接输出，效果优于高层解码器输出'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有DETR架构的音频片段检索（AMR）模型仅将帧级显著性序列作为训练阶段的辅助输出，未挖掘其推理阶段的实用价值。
### 方法关键点
提出基于SED启发的无参数分割规则，直接将帧级显著性序列转换为排序后的候选音频片段，无需依赖解码器预测，完全基于帧级时序信息完成检索任务。
### 关键结果
在CASTELLA数据集上，显著性预测在QD-DETR、CG-DETR的18组实验中全面优于同源模型的解码器预测；QD-DETR替换推理输出后R1@0.7从21.0提升至36.1，即使各自取最优epoch对比仍有7~15个点的优势；短片段（平均时长≤2s）场景下提升更显著，R1@0.7从6.3升至27.8；仅TR-DETR效果反向，说明显著性构造方式会影响效果，解码器监督仍对显著性预测有增益，训练与推理阶段的作用存在差异。
