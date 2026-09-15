---
title: 'Inherited Heads: Audio language models track speakers with their text backbone''s
  attention, and an attention-mass ranking retrieves a different set'
title_zh: 音频语言模型可复用文本主干注意力头实现指定说话人追踪
authors:
- Bojro Das
affiliations:
- Cornell University
arxiv_id: '2609.14174'
url: https://arxiv.org/abs/2609.14174
pdf_url: https://arxiv.org/pdf/2609.14174
published: '2026-09-12'
collected: '2026-09-15'
category: LLM
direction: 大模型注意力机制 · 多模态模型迁移
tags:
- Attention Head
- Audio LLM
- Model Steering
- Zero-shot Transfer
- Attention Ranking
one_liner: 发现音频大模型可复用同源文本大模型的注意力头，无需训练实现高精度指定说话人描述转向
practical_value: '- 做多模态Agent（语音客服、语音导购、音频内容理解）时，无需微调模型，仅需干预不到10%的注意力头即可实现输出定向控制，大幅降低落地成本

  - 注意力头筛选优先采用「注意力随Query变动幅度归一化排序」方法，比传统按注意力权重排序的方案降低98%以上的无效输出占比

  - 跨模态模型的特定任务能力可直接从同源文本大模型迁移，无需模态相关数据参与筛选，适合缺乏标注数据的多模态业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有音频大模型在多说话人场景下的指定说话人内容描述准确率仅6%~16%，低于16.7%的随机猜测水平，效果无法满足落地需求。
### 方法关键点
1. 无需任何训练，仅对模型占比不到10%的注意力头的attention logits加固定偏置，即可定向控制输出指向指定说话人；
2. 可直接从同源文本大模型的文本版同类任务中筛选Top100注意力头迁移使用，无需音频数据参与筛选；
3. 对比两种注意力头排序策略：传统按目标段注意力权重排序，以及新增的按注意力随query变动幅度的归一化排序。
### 关键结果
1. 直接筛选音频模型头干预，准确率达90.7%~99.0%；
2. 迁移同源文本模型头，准确率达80.8%~95.0%，两类头重合度达66%~74%；
3. 归一化排序法的无效输出占比仅1.0%，远低于传统方法的69.7%。
