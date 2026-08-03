---
title: 'Think2Go: Generative Next POI Recommendation with LLM Reasoning'
title_zh: Think2Go：结合大语言模型推理的生成式下一个POI推荐框架
authors:
- Zhuang Zhuang
- Shanshan Feng
- Hangwei Qian
- Mingqi Yang
- Heng Qi
- Yanming Shen
- Baocai Yin
affiliations:
- Dalian University of Technology
- Wuhan University
- A*STAR
- South China University of Technology
arxiv_id: '2607.28997'
url: https://arxiv.org/abs/2607.28997
pdf_url: https://arxiv.org/pdf/2607.28997
published: '2026-07-31'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · LLM推理优化Semantic ID理解
tags:
- POI Recommendation
- Semantic ID
- Generative Recommendation
- GRPO
- SFT
- Reinforcement Learning
one_liner: 统一SFT与RL推理范式，通过双维度优势校准提升LLM对Semantic ID的理解，优化生成式下一个POI推荐性能
practical_value: '- 生成式推荐场景可复用「SFT+RL联合训练」架构：通过Self-Correct token桥接记忆（SFT优化答案正确性）与探索（RL优化推理轨迹），避免传统SFT后RL训练的灾难性遗忘问题，平衡记忆留存与探索能力

  - RL优化阶段可复用双维度优势校准trick：1）用核密度估计计算输入prompt与用户历史行为的相似度作为认知不确定性权重，向难例倾斜探索资源；2）用当前样本reward与最大reward的比值做难度感知缩放，避免不同难度样本更新强度一致的问题，有效缓解熵崩塌

  - 生成式推荐的奖励设计可参考渐进式规则：先给格式达标奖励，再给部分正确的细粒度奖励，解决RL训练初期reward稀疏问题，加速收敛

  - Semantic ID类生成式推荐的评估可增加跨域/ID分类任务，验证模型对ID语义的真实理解能力，而非仅记忆训练样本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
下一个POI推荐需要挖掘用户历史签到的复杂时空偏好，传统方法依赖人工设计的特征交互，泛化性差；现有LLM生成式POI推荐仅做SFT，对Semantic ID的语义理解不足，且未利用推理能力，在用户行为稀疏场景下效果受限；同时现有RL推理方法忽略样本难度差异，易出现熵崩塌、训练不稳定问题。

### 方法关键点
- 统一SFT+RL训练架构：模型输出结构为`Think->Go->Self-Correct->Answer，Answer段计算交叉熵损失优化记忆能力，Think+Go段计算RL损失优化推理能力，联合优化避免遗忘
- 校准优势策略优化（CAPO）：1）用核密度估计计算当前query与用户历史的时空相似度，得到认知不确定性权重，自适应调整优势信号，鼓励难例探索；2）提出难度感知奖励差（DRG），用当前奖励与最大奖励的比值缩放优势，适配不同样本难度，避免统一更新强度的问题；3）渐进式奖励设计，先奖励格式正确，再按语义匹配度给细粒度奖励，解决RL初期reward稀疏问题。

### 关键结果
在NYC、TKY、CA三个公开POI数据集上，对比15个基线，Acc@1比最强传统基线ROTAN分别提升23.86%、31.77%、17.47%，比最强LLM基线GNPR分别提升6.33%、5.78%、7.49%；跨域迁移性能优于GNPR最多6.04%，Semantic ID分类准确率比GNPR最高提升58.96%。

最值得记住的一句话：给生成式推荐增加推理能力，不仅能提升推荐效果，还能真正增强模型对Semantic ID的语义理解，大幅提升跨域泛化性。
