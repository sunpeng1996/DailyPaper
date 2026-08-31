---
title: 'LMSM: LLM Security Framework Inspired by Linux Security Modules'
title_zh: LMSM：受Linux安全模块启发的大语言模型安全框架
authors:
- XiuYu Zhang
- Bonan Ruan
- Junfeng Fang
- An Zhang
- Tat-Seng Chua
- Zhenkai Liang
affiliations:
- National University of Singapore
- University of Science and Technology of China
arxiv_id: '2608.25697'
url: https://arxiv.org/abs/2608.25697
pdf_url: https://arxiv.org/pdf/2608.25697
published: '2026-08-25'
collected: '2026-08-31'
category: LLM
direction: 大语言模型 · 运行时安全管控框架
tags:
- LLM Security
- LLM Serving
- Safety Control
- Sparse Autoencoder
- vLLM
one_liner: 借鉴Linux安全模块架构解耦LLM安全检测与服务逻辑，实现低损耗高可扩展的大模型运行时安全管控
practical_value: '- 搭建Agent/LLM4Rec线上服务时可复用该解耦架构，将内容安全检测逻辑与大模型推理服务分离，新增检测规则无需修改核心服务代码

  - 线上LLM服务部署安全能力时可参考其性能优化方案，32并发下吞吐量仅损失不到2%，兼顾安全管控与业务性能要求

  - 可将SAE、密集探针等多种模型内部信号检测能力接入统一框架，组合多安全规则降低恶意prompt绕过概率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM分层防御仍易被恶意prompt绕过，可解释性方法输出的模型内部信号用于安全管控时，通常与各自的校准、策略、干预代码强耦合，新增检测能力需要大量集成工作，无法沉淀通用防御能力。
### 方法关键点
借鉴Linux安全模块的职责分离设计，提出LMSM三层架构：
1. 安全后端输出校准后的检测证据，支持SAE、转码器、任务适配密集探针等多种检测能力
2. 带版本的策略层基于可信请求上下文执行安全规则
3. 独立网关控制缓存的生成结果是否放行，完全解耦调解逻辑与策略效果，修改后端/规则/调度无需重构核心服务逻辑
### 关键结果
在Qwen3-4B上测试，LMSM-Checkpoint将HarmBench攻击成功率从39.20%降至3.32%，XSTest误拒率仅从2.40%升至4.40%，32并发序列下保留无监控服务98.14%的吞吐量。
