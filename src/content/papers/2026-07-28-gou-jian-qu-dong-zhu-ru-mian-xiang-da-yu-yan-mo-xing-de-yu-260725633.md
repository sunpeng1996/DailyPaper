---
title: 'Construction-Driven Injection: Linguistically-Grounded Edit-Based Code-Mixing
  Fingerprints for Large Language Models'
title_zh: 构建驱动注入：面向大语言模型的语言学编辑型码混合指纹
authors:
- Yongyi Cui
- Yue Li
- Tianbao Jiang
- Xin Yi
affiliations:
- East China Normal University
arxiv_id: '2607.25633'
url: https://arxiv.org/abs/2607.25633
pdf_url: https://arxiv.org/pdf/2607.25633
published: '2026-07-28'
collected: '2026-07-30'
category: LLM
direction: 大语言模型 · 所有权水印注入
tags:
- LLM Watermark
- Fingerprint Injection
- Code-Mixing
- Null Space Projection
- Ownership Verification
one_liner: 提出联合优化构建与注入的LLM水印框架，解决现有水印易误激活、易被困惑度检测过滤的问题
practical_value: '- 训练自有商用LLM/RecSys大模型时，可复用该框架注入不可擦除所有权水印，避免模型被盗用商用

  - 码混合语义密度替换、语法偏置混合的trick可迁移到Query改写/风控场景，生成低困惑度难过滤的特殊触发词

  - 空投影+跨语言对齐的权重更新方式可复用在LoRA微调场景，实现目标能力注入同时最小化原有模型性能损失'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM指纹方案存在两大核心缺陷：自然语言指纹易出现误激活，乱码指纹易被困惑度检测过滤；且指纹构建与注入阶段完全解耦，无法利用触发词的语言学结构做针对性优化，所有权验证能力易被微调、量化等篡改操作破坏。
### 方法关键点
1. 提出LCF模块生成码混合指纹：基于低资源语言组合，通过语义密度替换规则、语法偏置混合生成触发词，困惑度远低于乱码基线，同时避免自然语言指纹的误激活问题
2. 提出LCFEdit模块实现构造感知的指纹注入：基于高资源多语言表征的空投影保证原有知识不被破坏，新增跨语言对齐步骤将权重更新导向指纹语言的表征子空间，提升注入稳定性
### 关键结果
多维度测评验证，方案可实现持久所有权验证，误激活率较自然语言指纹方案降低90%以上，注入后模型原有效用损失可忽略，可抵抗微调、量化等常见篡改操作，所有权验证准确率保持99%以上
