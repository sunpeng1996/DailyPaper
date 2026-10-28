---
title: Did the Model Use That? Counterfactual Training Boosts Self-Attribution in
  Language Models
title_zh: 反事实训练提升大语言模型自归因可信度
authors:
- Zikai Zhou
- Jiacheng Sang
- Yilin Xu
- Yufei Jin
- Monica S. Lam
affiliations:
- Stanford University
- Duke University
- Emory University
- UCLA
arxiv_id: '2610.35295'
url: https://arxiv.org/abs/2610.35295
pdf_url: https://arxiv.org/pdf/2610.35295
published: '2026-10-25'
collected: '2026-10-28'
category: Training
direction: 大模型训练 · 自归因能力优化
tags:
- Self-Attribution
- Counterfactual Training
- LoRA
- Faithfulness
- LLM
one_liner: 提出无需人工标注的CREDIT反事实训练方法，直接监督最终输出的自归因语句，大幅提升准确率
practical_value: '- 搭建RAG类电商导购/客服Agent时，可复用CREDIT的无标注反事实标注流程，轻量化LoRA微调让模型准确说明回答是否依赖检索的商品/活动信息，降低错误检索带来的信任风险

  - 无需监督CoT中的归因内容，直接监督最终对用户可见的归因语句即可，推理侧的归因不会自动同步到最终回答，可大幅节省标注和训练成本

  - 跨场景部署时，训练阶段尽量覆盖多类外部信息（用户偏好、检索结果、工具返回等），单类信息训练会导致其他场景的归因准确率明显下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型无法准确披露回答是否依赖外部输入：要么漏报有实际影响的外部信息，要么错报未发挥作用的信息，仅监督推理链中的归因也不会同步到最终输出，用户无法区分回答来自模型自有知识还是外部输入，在RAG导购、推荐解释、智能客服等场景会带来可信度问题。
### 方法关键点
- 提出CREDIT训练pipeline，全程自动生成反事实标签无需人工标注：固定问题，移除外部信息后跑N次得到反事实回答，对比原回答判断外部信息是否有影响
- 仅替换最终输出的归因语句，保留原推理过程和回答内容，用LoRA轻量化微调，无需修改基座模型结构
- 训练覆盖4类外部信息：用户建议、检索段落、工具输出、其他AI回答，平衡正负样本比例
### 关键结果
- 测试集上4款开源模型的自归因平衡准确率从0.49~0.80提升到0.85~0.90，超过所有11款测试的前沿闭源模型（闭源最高仅0.66）
- 仅监督推理链归因的VFT基线推理侧准确率达0.74，但最终回答准确率仅0.50（和随机水平相当），远低于CREDIT的0.86
- 训练覆盖多类外部信息时可部分迁移到未见过的信息类型，单类训练会导致其他类型的归因准确率下降
> 最值得记住的一句话：大模型的推理侧认知不会自动同步到用户可见的最终输出，要得到可信的对外归因，必须直接监督最终输出的归因语句
