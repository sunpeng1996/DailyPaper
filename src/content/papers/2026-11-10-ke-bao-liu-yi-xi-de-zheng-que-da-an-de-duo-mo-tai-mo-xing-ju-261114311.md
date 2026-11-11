---
title: Multimodal Abstention That Preserves Acquired Correct Answers
title_zh: 可保留已习得正确答案的多模态模型拒答机制
authors:
- Jinyuan Zhang
affiliations:
- Hubei University
arxiv_id: '2611.14311'
url: https://arxiv.org/abs/2611.14311
pdf_url: https://arxiv.org/pdf/2611.14311
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: 多模态大模型 · 拒答能力优化
tags:
- Multimodal LLM
- Abstention
- SFT
- Linear Probe
- Threshold Calibration
one_liner: 提出无回退多模态拒答方法ReFrain，不损失SFT习得能力的同时提升不可答问题拒答准确率
practical_value: '- 业务微调后的LLM/多模态模型新增拒答能力时，可复用ReFrain的首token logits线性探针+阈值校准思路，避免破坏原有已习得的业务能力，适用于商品问答、内容审核等场景

  - 可基于业务场景设置拒答容忍预算（如允许丢失0.5%的正确回答），在保证核心业务效果不变的前提下最大化无效query的拒答率，降低大模型幻觉输出

  - 无需对原有模型做二次SFT即可实现拒答优化，节省微调成本，适合已上线的大模型应用快速迭代拒答能力'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
已完成任务SFT的多模态模型新增拒答能力时，易丢失原有已习得的正确回答，甚至抵消SFT收益，传统拒答微调的能力回退成本高。
### 方法关键点
提出ReFrain无回退拒答框架，核心为三点：1）基于首token logits的线性探针判断是否拒答；2）在留出图像簇上做阈值校准，可自定义允许丢失正确答案的容忍预算；3）确定性否决机制，仅将拒绝输出替换为「以上都不是」，其余原有响应完全保留，零预算下校准集无效果损失。
### 关键结果
在Qwen2.5-VL-3B上，零预算下完全保留全部57个SFT习得的正确回答，拒答准确率提升7.30pp；0.5%预算下拒答准确率达74.05%，仅丢失8个正确回答，效果远超EmbLoRA基线；独立测试集上0.5%预算点拒答准确率66.05%，比EmbLoRA高32.72pp，无正确回答损失。
