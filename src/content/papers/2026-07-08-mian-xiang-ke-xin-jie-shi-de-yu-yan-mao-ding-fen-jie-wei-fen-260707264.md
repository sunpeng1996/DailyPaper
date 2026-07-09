---
title: 'Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for
  Faithful Explanation'
title_zh: 面向可信解释的语言锚定分解：为分类器依赖概念自动命名
authors:
- Ahsan Habib Akash
- Dipkamal Bhusal
- Stacey Jones
- Donald A. Adjeroh
- Binod Bhattarai
- Prashnna Kumar Gyawali
affiliations:
- West Virginia University
- Rochester Institute of Technology
- University of Aberdeen
- University College London
- O Analytics
arxiv_id: '2607.07264'
url: https://arxiv.org/abs/2607.07264
pdf_url: https://arxiv.org/pdf/2607.07264
published: '2026-07-08'
collected: '2026-07-09'
category: Multimodal
direction: 多模态可解释 · 语言锚定概念分解
tags:
- Interpretability
- LLM
- CLIP
- Post-hoc Explanation
- Matrix Factorization
one_liner: 推出无需修改原模型的post-hoc框架LAD，生成兼具可读性与忠实性的视觉分类器决策解释
practical_value: '- 电商多模态商品分类/审核场景可复用LAD思路，无需重训模型即可输出可解释的决策依据（比如识别「短袖」「纯棉」等特征对应的商品区域），降低bad
  case排查成本

  - 构建生成式推荐的商品语义标签体系时，可借鉴「LLM生成候选概念+CLIP空间定位」的pipeline，自动挖掘商品细粒度属性，无需人工标注大量训练数据

  - 多模态Agent交互场景下，可将LAD输出的命名化概念作为跨模态输入的中间语义符号，降低跨模态信息对齐歧义，提升多轮决策的可解释性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉分类器可解释方案存在固有trade-off：post-hoc概念方法输出的特征与模型行为一致但无人类可读命名，自带命名的可解释方案需要重训或修改原模型，无法适配高风险场景下已上线的固定模型需求。
### 方法关键点
Language-Anchored Decomposition（LAD）是一套post-hoc框架，全程无需修改原模型：1）对每个分类目标，调用LLM生成候选概念词汇表；2）通过CLIP相似度映射定位概念对应的图像区域，得到语言锚定的系数矩阵；3）反转传统非负矩阵分解流程，固定系数矩阵仅学习概念基来重建冻结编码器的激活值，将命名作为结构约束，完整保留原模型的特征几何特性。
### 关键结果
在自然图像、场景、医学影像三类基准上，LAD输出的空间定位解释在概念插入/删除测试下均与决策强相关，是唯一能同时输出稳定人类可读概念名的方案；移除语言锚定后，归因忠实度完全下降但模型准确率不受影响。
