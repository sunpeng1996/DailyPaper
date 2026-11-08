---
title: LLM-Assisted Label Noise Correction for EEG-Based Sleep Stage Classification
title_zh: 大语言模型辅助修正标签噪声的EEG睡眠阶段分类方法
authors:
- Elmira Salari
- Shruti Kshirsagar
affiliations:
- Wichita State University
arxiv_id: '2611.08311'
url: https://arxiv.org/abs/2611.08311
pdf_url: https://arxiv.org/pdf/2611.08311
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: LLM辅助训练数据标签降噪
tags:
- LLM
- Label Noise Correction
- Training Data Processing
- Lightweight Deployment
one_liner: 提出仅训练阶段运行的LLM辅助标签过滤pipeline，提升分类精度同时保留轻量推理架构
practical_value: '- 可复用「小模型预跑筛选低置信样本→LLM结合规则与上下文核验标签→重训小模型」的标签降噪pipeline，适配推荐系统训练数据清洗场景

  - 训练阶段用LLM做数据清洗、推理阶段保留轻量小模型的架构思路，可平衡推荐效果与推理耗时，适配高QPS的电商/广告业务

  - 给低置信样本补充上下文特征再喂给LLM做标签判定的技巧，可提升标签清洗的准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
EEG睡眠阶段分类依赖人工标注训练标签，存在标注者分歧、系统性标注误差等噪声问题，大幅限制深度学习模型性能；同时穿戴设备端部署要求推理架构轻量，无法直接引入大模型。
### 方法关键点
1. 先在原始带噪数据集上训练1.3M参数的轻量TinySleepNet，提取每个30s epoch的SoftMax置信度，筛选低置信样本
2. 将低置信样本的EEG频谱特征、周围序列上下文与AASM睡眠评分规则一起输入LLaMA 3.1，判定标签为RELIABLE或SUSPICIOUS，移除可疑样本
3. 用清洗后的数据集重新训练TinySleepNet，推理阶段仍使用原始轻量模型，无额外计算开销
### 关键结果
在Sleep-EDF扩展数据集上做20折交叉验证，整体准确率从81.8%提升至84.6%，Macro F1-score从75.6%提升至77.4%，REM检测效果增益尤为显著。
