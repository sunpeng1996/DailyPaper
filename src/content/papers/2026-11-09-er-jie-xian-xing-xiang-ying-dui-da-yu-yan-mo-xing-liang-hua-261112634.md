---
title: How Far Does Second-Order Linear Response Predict Quantization Mismatch? Pre-Registered
  Measurements on Five Language Models
title_zh: 二阶线性响应对大语言模型量化失配的预测效果评测：5个模型的预注册实验
authors:
- Dezhen Lu
- Zixiang Ni
affiliations:
- University of Tübingen
- Xi’an Jiaotong University
arxiv_id: '2611.12634'
url: https://arxiv.org/abs/2611.12634
pdf_url: https://arxiv.org/pdf/2611.12634
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: 大语言模型量化 · 损失预测
tags:
- Quantization
- Fisher Information
- LLM Serving
- Model Compression
- PTQ
one_liner: 通过5个LLM的预注册实验验证二阶Fisher量化损失预测可靠性，提供可落地的量化筛选器方案
practical_value: '- 部署LLM做生成式推荐/Agent推理时，可直接复用论文提出的量化筛选器，8分钟即可完成3种量化格式的评估，大幅降低选型成本

  - LLM推理服务选量化格式时，优先用fp32计算反向梯度+5%截断平均的二阶Fisher预测方案，10/12场景下预测误差小于15%

  - 若用bf16做反向梯度计算，需过滤bf16/fp32比值>10的异常序列，避免4倍左右的预测误差

  - 量化格式选型遇到MoE模型时需额外注意：小扰动下MoE的KL散度呈亚线性增长，二阶预测误差可达27倍，建议直接实测验证'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM部署时需为不同业务场景（生成式推荐文案、Agent推理等）选择适配的量化格式，逐组实测任务性能成本极高；行业普遍采用二阶线性响应公式（KL≈1/2Δ⊤FΔ）基于Fisher信息预测量化损失，但该方法的可靠性缺乏系统验证，工程实现中的数值误差影响也不明确。

### 方法关键点
- 覆盖5个主流开源LLM：Qwen3-4B/8B/32B、OLMo-2-7B、Mistral-7B-v0.3，验证3种主流量化方案（通道级int8、张量级fp8、组级int4）
- 所有实验规则预注册，提前冻结预测逻辑、评估指标、校验规则，避免后验调参偏置
- 对比不同梯度精度（bf16/fp32）、平均方式（普通平均/5%截断平均）、估计形式（元素级对角线/张量块）的预测效果

### 关键结果
- 相对预测准确率达99%以上：跨16倍扰动范围、int4组大小、舍入模式的预测误差≤5%，随机舍入的KL提升预测误差仅0.3%
- 采用fp32梯度+5%截断平均的绝对预测方案：在Qwen3-4B、OLMo-2上10/12场景误差≤15%；bf16梯度若未过滤异常序列，预测误差可达4倍
- 最终落地的量化筛选器在未见过的Mistral-7B-v0.3上6个测试场景全落在预测区间内，vLLM吞吐量预测误差≤0.4%，全流程仅需0.77 GPU小时

### 最值得记住的一句话
32B以上大模型int4量化易出现单张量误差对齐问题，MoE模型二阶预测误差最高可达27倍，低预算选型优先用fp32梯度+截断平均+张量块的预测方案
