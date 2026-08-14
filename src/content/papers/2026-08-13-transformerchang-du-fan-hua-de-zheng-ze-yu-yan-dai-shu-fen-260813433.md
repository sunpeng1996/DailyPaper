---
title: Algebraic Decomposition Theory for Transformer Length Generalization
title_zh: Transformer长度泛化的正则语言代数分解理论与多项式决策算法
authors:
- Andy Yang
- Blerta Veseli
- Corentin Barloy
- Michaël Cadilhac
- Andreas Krebs
- Charles Paperman
- Howard Straubing
- Michael Hahn
affiliations:
- University of Notre Dame
- Saarland University
- Ruhr University Bochum
- DePaul University
- University of Tübingen
arxiv_id: '2608.13433'
url: https://arxiv.org/abs/2608.13433
pdf_url: https://arxiv.org/pdf/2608.13433
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: 大模型基础理论 · Transformer长度泛化
tags:
- Transformer
- Length Generalization
- Formal Language
- Algebraic Decomposition
- C-RASP
one_liner: 提出正则语言下Transformer长度泛化的代数刻画与多项式时间决策算法
practical_value: '- 做Agent工作流/结构化生成（如JSON/订单格式校验）时，可先将规则映射为正则语言，用论文给出的多项式决策算法预判Transformer是否能长度泛化，避免上线后长序列出错

  - 长序列推荐/搜索的规则类任务（如用户行为序列状态校验、促销规则匹配），若属于C-RASP类可直接用Transformer做长序列推理，不需要额外做长度扩展训练

  - 做LLM长序列微调时，若任务不满足C-RASP条件，可调整任务规则（简化状态跳转逻辑）使其落入C-RASP范畴，大幅提升长序列泛化效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Transformer的长度泛化能力缺乏可量化的判定标准，尤其是对正则语言这类基础规则类任务，现有理论无法解释结构高度相似的正则语言为何长度泛化效果存在显著差异，工业界只能通过大量实验验证长序列任务的泛化性，成本极高。
### 方法关键点
- 突破传统Krohn-Rhodes有限半群分解理论的局限，将代数分解框架扩展到整数加法群，提出基于类型化幺半群和迭代wreath乘积的C-RASP代数刻画，证明正则语言属于C-RASP等价于其句法幺半群属于整数群的wreath乘积闭包。
- 设计多项式时间决策算法，通过迭代计算句法幺半群到整数群的关系态射，判定正则语言是否属于C-RASP，同时给出基于有限等式的快速必要（非充分）判定条件，可快速筛除无法泛化的任务。
### 关键实验
在125个覆盖不同类别的正则语言测试集上，模型训练序列长度上限为50，测试长度最高达500。C-RASP类语言在序列长度为训练集10倍时仍保持接近100%的准确率，非C-RASP类语言在超出训练长度后准确率快速下降至60%以下，预测准确率显著优于现有R-平凡、星-free等分类标准。

**最值得记住的结论**：Transformer对规则类长序列任务的泛化能力完全由任务对应的正则语言是否属于C-RASP决定，盲目增加训练数据或模型大小无法从根本上解决非C-RASP任务的长度泛化问题。
