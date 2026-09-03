---
title: 'From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection
  for Text Classification'
title_zh: 面向多相似标签分类的混淆感知检索与知识注入框架
authors:
- Manish Gupta
- Chaitanya Giri
- Jayasimha Talur
affiliations:
- Amazon
arxiv_id: '2609.01564'
url: https://arxiv.org/abs/2609.01564
pdf_url: https://arxiv.org/pdf/2609.01564
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: 大模型文本分类 · 消歧增强
tags:
- Text Classification
- Knowledge Injection
- Retrieval Augmentation
- Zero-shot Learning
- Cross-model Transfer
one_liner: 通过易混淆标签对识别、候选集扩充与配对消歧规则注入，无需微调提升大模型文本分类效果
practical_value: '- 电商商品类目分类、客服工单分类等高相似标签场景，可复用混淆伙伴扩充候选集的思路：先跑基线统计易混淆标签对，检索时补充对应标签，不用盲目提升K值就能大幅提升候选召回率，Flipkart
  L3场景下召回从86%升至98.1%

  - 无需微调即可降低推理成本：离线用大模型生成易混淆标签对的配对消歧规则，推理时注入给2B-20B小模型，Flipkart L3场景下小模型F1最高提升11.5pp，推理成本远低于调用大模型

  - 消歧规则优先用配对格式而非单标签描述：配对规则明确给出两个相似标签的区分边界，比独立的单标签描述能降低约4.8%的LLM选错概率，效果更稳定

  - 小样本/标签噪声多的业务场景优先选这套框架：仅用10%训练数据时F1达70.2，比微调RoBERTa高38.4pp，20%标签噪声下仍保持72.1的F1，抗扰动能力远强于微调模型'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型零样本分类在包含大量语义相似标签的类目体系（如电商商品类目、客服工单、法律文书）下表现极差，常规Top-K检索仅能缩小候选范围，无法解决相似标签的区分问题；而微调方案依赖大量干净标注数据，迭代成本高，难以应对标签变更、分布漂移等工业场景常见问题。
### 方法关键点
- 离线统计基线分类器的混淆矩阵，筛选覆盖≥75%训练误差的高频易混淆标签对，为每个标签定义混淆伙伴
- 推理阶段检索Top-K候选后，补充每个候选的混淆伙伴，无需提升K值即可大幅提升正确标签召回率
- 三阶段生成配对消歧规则：从错分样本抽取单例区分信号→汇总生成定向规则→合并双向规则为对称消歧规则，推理时将对应规则注入Prompt
### 关键实验结果
在法律LEDGAR、学术WOS、电商Flipkart三个数据集上测试，对比零样本、少样本、MIPROv2、GEPA、普通检索等基线：
- Qwen3-32B上全方法Macro F1最高提升10.0pp，Flipkart L3细分类目下比普通检索基线高4.4pp
- 大模型生成的规则可跨模型迁移，2B-4B小模型F1最高提升11.5pp，8-20B中模型最高提升11.1pp
- 抗扰动能力远优于微调模型：仅用10%训练数据时F1达70.2，比微调RoBERTa高38.4pp；20%标签噪声下仍保持72.1的F1
### 最值得记住的结论
针对大模型实际错分的标签对做定向增强，比通用Prompt优化、盲目扩大检索K值、甚至微调的投入产出比更高，尤其适合业务多变、标签迭代快的工业场景
