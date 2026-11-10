---
title: Phrase-Level Speculative Decoding on a Frozen Target
title_zh: 面向冻结大语言模型的短语级投机解码方法
authors:
- Madhusudhana Naidu
arxiv_id: '2611.12464'
url: https://arxiv.org/abs/2611.12464
pdf_url: https://arxiv.org/pdf/2611.12464
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- Speculative Decoding
- LLM Inference
- Parameter Efficient
- Frozen LLM
- Phrase Drafting
one_liner: 不修改冻结LLM与分词器，用超小MLP头实现短语级投机解码，参数效率远超EAGLE-3
practical_value: '- 电商/Agent场景LLM服务加速：可直接复用该框架，无需微调底座大模型，仅需针对业务场景（如客服话术、商品文案生成、订单通知）构造专属高频短语词典，训练3-20M的小MLP头即可获得1.5-2.5倍的推理提速，落地成本极低

  - 端侧Agent部署参考：8000词表的MLP头仅3.4M参数，占7B模型参数的0.08%，额外显存占用不到1GB，完全可以嵌入端侧智能助手、商品导购Agent等轻量场景

  - 领域收益预判技巧：针对高重复格式的业务场景（如商品属性描述、固定客服话术、结构化报表生成）优先落地，重复格式片段可贡献60%以上的加速收益，远高于通用对话场景

  - 管线兼容：该方法与现有树状投机解码（如EAGLE-3）正交，可直接叠加使用，无需修改现有推理管线，仅需新增短语映射模块即可进一步提升速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有投机解码方案均基于目标模型原生BPE词表做单token预测，受限于BPE预分词按空格切分的规则，无法将多词短语作为单个预测单元，单决策的token增益存在明显天花板；同时EAGLE-3等主流方案的draft模型参数达数百M，训练部署成本高，适配高分词生育率的小语种、垂直场景效率极低。

### 方法关键点
- 完全冻结目标LLM及其分词器，仅新增2层LayerNorm的轻量MLP头，输入为目标模型隐层状态，输出自定义短语级draft词表的logits
- 短语词表从目标模型生成的领域语料中挖掘，支持1-3词单元（含标点、格式符号），预测的短语通过最长匹配映射回原生BPE token序列
- 多token候选通过前缀树掩码在目标模型单次前向传播中完成验证，输出结果与贪婪解码完全一致，无精度损失
- 参数量与短语词表大小线性正相关：8000词表对应3.43M参数（仅占Qwen3-4B的0.085%），8万词表对应21.94M参数

### 关键结果
- 单A5000、batch1、Qwen3-4B底座：21.94M头在GSM8K提速2.391×，MATH-500提速2.444×，零样本MT-Bench提速1.544×
- 对比EAGLE-3：21.94M头（仅为EAGLE-3参数的10.1%）在GSM8K、MATH-500上速度超过EAGLE-3 tree-16配置，达到tree-60配置的91.5%、98.1%
- 验证开销仅4.2-5.5ms，为EAGLE-3的1/3~1/2，额外显存占用<0.75GB

### 核心结论
投机解码的核心瓶颈不是候选树的宽度深度，而是单个决策的token增益，垂直领域通过挖掘高频格式/短语单元，用超小模型就能拿到绝大多数加速收益
