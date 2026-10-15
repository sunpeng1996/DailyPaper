---
title: 'The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free
  Adaptation'
title_zh: COUNT：基于N-gram计数利用主机内存实现无训练适配的LLM扩展方法
authors:
- Ian Magnusson
- Noah A. Smith
- Pang Wei Koh
affiliations:
- University of Washington
- Allen Institute for AI
arxiv_id: '2610.20456'
url: https://arxiv.org/abs/2610.20456
pdf_url: https://arxiv.org/pdf/2610.20456
published: '2026-10-13'
collected: '2026-10-15'
category: LLM
direction: LLM效率优化 · 无训练域适配
tags:
- N-gram
- LLM Efficiency
- Training-free Adaptation
- Host Memory Optimization
- Scaling Law
one_liner: 利用预计算N-gram统计量复用LM unembedding矩阵，靠廉价主机内存提升LLM性能并支持无训练域适配
practical_value: '- 做垂直域LLM服务（如电商客服、商品文案生成）时，可预计算垂直域N-gram统计表，推理时直接替换通用表，无需微调即可提升域内效果，成本极低

  - LLM训练/推理资源紧张的场景下，采用COUNT方案将N-gram统计量放在廉价主机内存，省出GPU内存用于backbone扩参，性价比远高于添加可学习N-gram嵌入

  - 生成式推荐（GenRec）场景下，可基于用户行为序列、商品库预计算N-gram continuation统计，作为额外输入嵌入提升推荐结果的相关性与流畅度，无需新增可学习参数'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有可学习N-gram嵌入方案需占用昂贵GPU内存存储参数与优化器状态，与LLM backbone争抢显存资源，且无法无训练适配新领域；而廉价主机内存长期未被充分利用，传统计数型N-gram方法的价值未被有效结合到Transformer输入层优化中。
### 方法关键点
- 离线预计算语料的N-gram历史到top-K高频后续token的映射与stupid backoff得分，存储在主机内存，无新增可学习参数
- 复用LLM自身的unembedding矩阵作为基，加权求和高频后续token的未嵌入向量得到COUNT嵌入，和token嵌入相加作为Transformer输入
- 支持推理时直接替换为域专属N-gram统计表，或压缩表大小适配低内存部署环境，无需任何微调
### 关键结果
在Dolma 3语料上训练60M~1B参数的OLMo-core系列模型，对比标准Transformer、可学习N-gram嵌入基线：
1. 同等计算预算下，COUNT的LM验证loss等效于标准Transformer多投入46%~89%计算量的效果，下游任务loss等效于多投入6%~56%计算量的效果
2. 推理时替换为垂直域N-gram表，数学、法律域任务loss最高下降0.05BPB，准确率最高提升3个百分点
3. 训练/推理吞吐量仅比标准Transformer低2%~7%，额外开销极低

最值得记住：昂贵GPU显存应优先分配给LLM backbone参数，非参数化统计信息完全可以利用廉价主机内存存储，同等资源下能带来显著性能收益。
