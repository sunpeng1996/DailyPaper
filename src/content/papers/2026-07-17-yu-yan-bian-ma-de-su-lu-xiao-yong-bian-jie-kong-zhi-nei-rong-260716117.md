---
title: 'Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and
  Pixels Under Controlled Linguistic Content'
title_zh: 语言编码的速率-效用边界：控制内容下Token、字节与像素的对比
authors:
- Ingo Ziegler
- Martin Krebs
- Desmond Elliott
affiliations:
- Department of Computer Science, University of Copenhagen
arxiv_id: '2607.16117'
url: https://arxiv.org/abs/2607.16117
pdf_url: https://arxiv.org/pdf/2607.16117
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 大模型文本编码 · 速率效用权衡
tags:
- Text Encoding
- Tokenization
- Byte Encoding
- Pixel Encoding
- Multilingual LLM
one_liner: 控制内容与下游容量的前提下，量化三种文本编码的效率与任务适配边界
practical_value: '- 多语种电商内容处理：同脚本跨语言检索/对齐场景优先选字节编码，性价比比Token高1.4~1.6倍，跨多脚本场景仍用Token更划算

  - 商品图文理解、OCR、标题纠错等需保留表面形式的任务优先选像素编码，训练成本比Token低30%~70%，精度更高

  - 用户评论、商品内容的主题分类、语义标签生成类任务默认选Token编码，相同FLOPs下精度比字节、像素高40%~100%，抗压缩能力更强

  - 中文等非拉丁脚本低算力边缘场景可尝试像素编码，中文场景下像素编码主题分类精度可达Token的60%，仅需一半算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
此前不同文本编码的对比受模型结构、语言资源差异干扰，无法区分性能差异来自编码本身还是输入内容量、模型容量的区别，业务场景缺乏可落地的编码选择量化依据。

### 方法关键点
- 采用SIB-200人工翻译平行数据集，覆盖13种语言、5种脚本，严格控制输入内容完全一致，排除内容差异干扰
- 对比三种编码：按语言域单独训练的32k词表SentencePiece Token、原生UTF-8字节、36×32灰度块的像素渲染编码
- 引入Perceiver风格共享瓶颈层，通过调整瓶颈维度D控制下游可用容量，绘制速率-效用边界，分离输入序列长度、latent容量、任务信息留存三个常被混淆的变量
- 评估三类核心效用：表面形式留存、跨语言句子对齐、主题分类，同时统计训练FLOPs量化计算成本

### 关键结果
- 表面形式留存任务：高容量下像素Recall@1达0.97~0.99，低容量（D<10）同脚本场景字节反超
- 跨语言对齐任务：同脚本场景下字节Recall@1达0.45~0.47，比Token高60%~70%，仅多消耗1.4~1.6倍FLOPs；跨多脚本场景字节优势消失，与Token性能相当但算力消耗高4.2倍
- 主题分类任务：Token的macro-F1达0.46~0.63，比字节高70%~90%、比像素高130%~200%，且性能到D=8几乎无衰减

**最值得记住的结论**：不存在通用最优的文本编码，编码选择是速率-效用的权衡，取决于任务类型、语言脚本混合情况、可用容量与计算预算。
