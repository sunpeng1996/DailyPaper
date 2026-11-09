---
title: Reconstructing LLM Lineage Trees via Fine-Tuning Path Inference
title_zh: 基于微调路径推断的大语言模型谱系树重建方法
authors:
- Sota Ogawa
- Shojiro Yamabe
- Daiki Nishiyama
- Jun Sakuma
affiliations:
- Institute of Science Tokyo
- RIKEN
arxiv_id: '2611.08866'
url: https://arxiv.org/abs/2611.08866
pdf_url: https://arxiv.org/pdf/2611.08866
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 大语言模型 · 微调谱系追溯
tags:
- LLM
- Fine-tuning
- Model Provenance
- Gray-box
- Log-likelihood
one_liner: 灰盒场景下通过不对称对数似然偏差构建有向生成树，实现LLM微调谱系树重建
practical_value: '- 自研LoRA微调模型资产溯源场景可复用不对称log-likelihood偏差度量方法，低成本确认衍生模型的父节点归属，规避License合规风险

  - 对外采购微调LLM时，可采用仅需推理输出log-likelihood的灰盒验证方案，无需获取权重即可确认模型微调来源，排查恶意植入漏洞

  - 多版本业务LLM迭代时，可基于该方法构建模型谱系树，快速定位不同版本性能差异的根源，优化迭代路径'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前大量公开微调LLM的来源仅依赖自报告，无可靠验证方案，无法支撑外包微调审计、衍生模型License合规校验、父模型传递漏洞追溯需求；现有方法仅支持成对推导检测或无向谱系估计，有向谱系树重建要求白盒访问模型权重，落地限制大。
### 方法关键点
1. 灰盒访问场景下仅需获取teacher-forced log-likelihood，无需访问模型权重；
2. 基于微调提升训练数据log-likelihood、子模型继承父模型该特征的特性，定义不对称逐任务log-likelihood偏差作为微调历史痕迹，为每对有序模型计算边权；
3. TRACE-Edge方法可求解最大有向生成树，无超参数、无需预设树结构约束。
### 关键结果
在3个基础模型、7个任务构建的25个模型树上测试，使用微调样本探测时父节点匹配准确率达0.74；使用同分布held-out探测样本时，平均性能优于输出相似度基线。
