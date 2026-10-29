---
title: Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual
  Uncertainty Collapse
title_zh: 从感知不确定性崩塌视角揭示视频RLVR中的捷径放大效应及优化方案
authors:
- Jiafeng Liang
- Xianhao Ou
- Tao Ren
- Rongchuan Mu
- Runxuan Liu
- Dandan Tu
- Ming Liu
- See-Kiong Ng
- Bing Qin
affiliations:
- 哈尔滨工业大学
- 鹏城实验室
- 新加坡国立大学
- 北京大学
- 华为技术有限公司
arxiv_id: '2610.37211'
url: https://arxiv.org/abs/2610.37211
pdf_url: https://arxiv.org/pdf/2610.37211
published: '2026-10-27'
collected: '2026-10-29'
category: Reasoning
direction: 多模态推理 · RL训练优化
tags:
- Multimodal LLM
- Video Reasoning
- RLVR
- Perceptual Uncertainty
- Policy Optimization
one_liner: 提出双焦点自蒸馏BSPO框架，缓解视频RLVR文本先验捷径放大，增强视觉推理忠实度
practical_value: '- 电商短视频/直播内容理解、商品信息抽取场景，可复用SCP视觉扰动方案，验证模型预测是否依赖真实视觉内容而非文本先验，降低AI审核、选品的幻觉错误

  - 多模态Agent执行视频内容理解、多步推理任务时，可借鉴PCA原则引导的信用分配思路，对推理关键token分配更高权重，提升复杂推理准确率

  - 采用RL做LLM/LMM后训练的场景，可复用视觉条件熵差指标，监控模型是否出现依赖先验的捷径学习问题，提前终止无效训练

  - 生成式推荐引入多模态内容作为推荐依据时，可借鉴BSPO双权重优化思路，平衡推荐准确性与内容相关性，避免过度依赖用户行为先验忽略新内容特征'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLVR是当前提升多模态大模型视频推理能力的主流后训练范式，但仅优化结果匹配度的训练模式会放大捷径效应：模型越来越倾向输出符合文本先验的答案，甚至在无对应视觉证据支撑时也优先选择高频答案，导致表面准确率提升但实际视觉推理忠实度下降，且缺乏可解释的训练动态指标识别该问题。

### 方法关键点
- 提出感知不确定性崩塌分析框架：对比视频条件预测熵与纯文本条件预测熵的差值（视觉条件熵差），量化模型置信度提升中来自视觉证据的贡献占比，发现RL训练过程中该差值持续下降，说明模型置信度提升主要来自文本先锐化而非视觉信息利用
- 设计BSPO双焦点自蒸馏优化框架，包含两个核心模块：①PCA原则引导信用分配：同批次对比正确与错误推理轨迹，提取可复用的推理原则，对推理敏感token分配更高权重，解决传统轨迹级优势分配一刀切的问题；②SCP捷径感知对比扰动：通过打乱帧顺序、裁剪局部区域、替换空白帧三种方式弱化关键视觉证据，对比扰动前后的预测分布差异，惩罚对视觉扰动不敏感的预测，强制模型依赖真实视觉内容
- 双权重优化：将PCA与SCP的分布差异信号归一化后，自适应调整原有RL优势的幅度，不改变原始优化方向，保留RLVR的任务性能提升能力

### 关键结果
在Qwen3-VL 4B/8B两个基线模型上，对比GRPO、DAPO等主流RLVR方法，在6个视频推理基准上平均提升1.3~6.2个百分点，其中复杂视频推理任务最高提升5.7个百分点，反事实测试集上捷径答案选择率比GRPO降低30%以上。

### 核心结论
多模态模型RL训练的表面准确率提升，未必代表模态信息利用能力提升，需通过跨模态的不确定性对比指标来监控优化的实际价值。
