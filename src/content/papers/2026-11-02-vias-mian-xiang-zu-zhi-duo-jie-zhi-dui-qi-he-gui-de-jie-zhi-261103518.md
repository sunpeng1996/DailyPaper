---
title: 'VIAS: Value-Isolating Activation Steering for Multi-Value Alignment and Compliance
  for Organisations'
title_zh: VIAS：面向组织多价值对齐合规的价值隔离激活调控方法
authors:
- Avni Mittal
- Avinash Anand
- Dikshant Kukreja
- Erik Cambria
- Rajiv Ratn Shah
- Sandipan Dandapat
affiliations:
- Microsoft India
- Singapore Institute of Technology
- IIIT Delhi
- Nanyang Technological University
- IIT Kanpur
arxiv_id: '2611.03518'
url: https://arxiv.org/abs/2611.03518
pdf_url: https://arxiv.org/pdf/2611.03518
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: LLM激活调控 · 多价值对齐
tags:
- Activation Steering
- Value Alignment
- Compliance
- LLM Alignment
- Contrastive Learning
one_liner: 提出价值隔离对比对构造方法，降低激活调控向量重叠，提升组织场景LLM多价值合规率
practical_value: '- 电商/客服Agent做平台规则对齐时，可复用VIAS的对比对构造逻辑：固定其他规则，仅增减单条规则生成正负样本，避免规则向量共线性，比全规则对比更适合多规则叠加场景

  - 激活调控无需修改模型权重，比LoRA微调成本更低、迭代更快，适合电商平台频繁变更的营销/合规规则，仅需更新对应规则的steering vector即可快速上线

  - 多规则向量融合时，可参考Gram-Schmidt正交化+SNR可靠性加权的方案，减少向量叠加时的抵消/干扰，提升多规则同时生效的成功率

  - 小样本效率高，仅需25%的标注对即可超过纯prompt的合规效果，适合冷启动的规则对齐场景，大幅降低标注成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
企业部署LLM Agent时需要严格对齐组织的合规规则与价值观，纯prompt无法保证稳定的合规率，传统激活调控方法生成的多价值向量高度共线性（余弦相似度0.91-0.94），本质是捕获通用合规信号，无法实现多价值的精准叠加调控，多规则同时满足的准确率极低。
### 方法关键点
- VIAS价值隔离对比对构造：同一用户场景下生成两组响应，一组提示包含全部相关价值，另一组仅移除目标价值，仅保留目标价值合规性翻转、其余价值合规率≥50%的样本对，计算目标价值的steering vector
- 支持两种向量融合模式：原始平均融合，以及基于Gram-Schmidt正交化+SNR可靠性加权的融合，降低向量间的干扰
- 推理时在固定Transformer层注入加权后的调控向量，无需修改模型权重，可与价值提示（VP）叠加使用
### 关键结果
在PROTECT工作场合合规数据集上测试，覆盖21种组织价值，800条测试场景，对比基线prompt、LoRA SFT、全价值对比激活调控等方案：VIAS+VP在Qwen2.5-7B上全标签价值合规率69.6%，Mistral-7B上75.2%，Phi-3.5-mini上72.6%，均优于纯prompt方案；VIAS将不同价值向量的平均绝对余弦相似度从0.91-0.94降至0.09-0.45，大幅降低向量共线性；仅需25%的标注样本即可超过纯prompt的合规效果。
> 最值得记住的一句话：多价值对齐的激活调控效果瓶颈不在向量融合策略，而在对比对的构造逻辑，隔离单变量的样本对才能生成可叠加的价值调控向量
