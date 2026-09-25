---
title: Parts-of-Speech as Emergent Categories in SAE Latent Space
title_zh: 稀疏自编码器(SAE)隐空间中作为涌现类别的词性
authors:
- Alessandro Bondielli
- Lucia Passaro
- Serena Auriemma
- Alessandro Lenci
affiliations:
- CoLingLab, Department of Philology, Literature and Linguistics, University of Pisa
- Department of Computer Science, University of Pisa
arxiv_id: '2609.29362'
url: https://arxiv.org/abs/2609.29362
pdf_url: https://arxiv.org/pdf/2609.29362
published: '2026-09-23'
collected: '2026-09-25'
category: LLM
direction: LLM可解释性 · SAE隐空间语言结构编码
tags:
- SAE
- Part-of-Speech
- Latent Space
- LLM Interpretability
- Morpho-syntactic Representation
one_liner: 通过词性探测实验验证SAE隐空间以分布式类别依赖形式编码形态句法信息
practical_value: '- 优化LLM推理特征筛选：可参考词性相关SAE隐特征组的稀疏性特征，裁剪无效特征降低推理时延，适配电商文案生成、query改写等场景的低延迟需求

  - 业务定制SAE验证方案：可复用本文基于受控语法类别探测SAE隐特征有效性的方法，验证自定义SAE的特征对齐效果

  - 语义特征分组参考：可借鉴分布式特征编码思路，对用户/物品语义特征做稀疏分组，提升RAG召回、生成式推荐的语义匹配准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
SAE是LLM可解释性分析的核心工具，但目前尚不明确其隐空间暴露的语言学结构组织形式，无法确定语言特征是由单个隐变量编码还是多特征分布式编码。

### 方法
以词性（PoS）分类为受控测试场景，从token级SAE激活值中探测形态句法信息的编码模式，对比开放/封闭词性类别的特征可恢复性差异，验证隐特征组的跨数据集稳定性。

### 结果
1. PoS类别可从SAE激活中高准确率恢复，但不存在隐变量与类别的一对一映射
2. 类别可恢复性并非来自词表记忆，开放与封闭词性类别的编码模式差异显著
3. 每个词性对应一组紧凑的稀疏隐变量，组内特征在跨集测试中保持稳定，相关词性的特征组存在重叠
4. 形态句法信息以分布式、类别依赖的形式存储在SAE隐空间，而非原子化语法特征
