---
title: The SIMPLE Law for Energy Cost of LLM Inference
title_zh: LLM推理能耗的SIMPLE定律
authors:
- Hiari Pizzini Cavagna
- Andrea Proia
- Daniele Cesarini
- Zeynep Kiziltan
- Andrea Bartolini
affiliations:
- University of Bologna
- CINECA
arxiv_id: '2611.03330'
url: https://arxiv.org/abs/2611.03330
pdf_url: https://arxiv.org/pdf/2611.03330
published: '2026-11-01'
collected: '2026-11-06'
category: LLM
direction: LLM推理能耗建模与预测
tags:
- LLM Inference
- Energy Consumption
- KV-cache
- GQA
- Energy Prediction
one_liner: 无需单模型校准的跨架构LLM推理能耗四参数预测模型，精度较SOTA提升3.1-3.5倍
practical_value: '- 做Agent/生成式推荐服务成本核算时，可直接用SIMPLE模型预估不同prompt长度、输出长度的推理能耗，无需实测即可完成大促资源规划、服务定价

  - 选型LLM用于长上下文Agent/推荐场景时，优先选择高GQA分组比的架构，同等参数下可降低最多3倍的每token推理能耗

  - 优化推理服务时，Agent长上下文请求优先开启prefix caching，可降低93%的prefill阶段能耗，剩余KV-cache成本可通过量化、缓存复用进一步优化

  - 带推理的生成式推荐场景，可基于SIMPLE定律找到推理token预算的平衡点，避免盲目增加CoT长度导致能耗增速远超精度收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM推理占全生命周期90%的能耗，现有能耗预测模型多为经验拟合，需要针对每个LLM单独校准，无法泛化到未部署的新架构，也未覆盖GQA等主流注意力机制，难以支撑架构选型、成本预估、Agent长上下文场景的能耗优化需求。
### 方法关键点
- 从Transformer计算、内存访问复杂度出发，推导覆盖MHA、GQA的推理复杂度闭式表达式，拆分prefill、decode两个阶段，进一步将decode拆分为KV-cache访问、next-token计算两部分
- 四参数SIMPLE定律仅需隐藏层维度d、层数L、KV/查询头比R三个架构超参数+输入输出长度即可预测能耗，无需单模型校准
- 每token能耗可拆解为prefill成本摊销、KV-cache累计成本、固定next-token成本三部分，可解释性极强
### 关键结果
在H100上的13款稠密LLM（覆盖OPT、LLaMA、Gemma、Qwen2等6个系列）推理trace上验证：
- 全数据集拟合R²达0.969，MAPE仅11.97%，精度较SOTA模型提升3.1-3.5倍，无需单模型校准
- 更高GQA分组比可降低最多3倍的每token能耗；Agent请求能耗是普通请求的13倍，开启prefix caching后仍高4.8倍
- 推理token预算的单位焦耳智能度存在峰值，过高或过低的预算都会导致IPJ下降最多3.14倍
### 核心结论
LLM推理能耗并不与参数规模线性相关，隐藏层维度、注意力结构、输入输出长度的组合才是核心决定因素
