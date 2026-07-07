---
title: When Words Predict Workload
title_zh: 基于文本语言学特征的LLM推理负载预测与边云路由网关
authors:
- Anubhab Banerjee
affiliations:
- Nokia Germany
arxiv_id: '2607.04951'
url: https://arxiv.org/abs/2607.04951
pdf_url: https://arxiv.org/pdf/2607.04951
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: LLM边云推理 · 负载预测动态路由
tags:
- LLM Inference
- Edge-Cloud Routing
- Linguistic Feature
- XGBoost
- GPU Memory Management
one_liner: 提出CPU侧轻量语言学负载预测网关，将边云路由错误率较token计数基线降低一个数量级
practical_value: '- 端侧LLM部署（如电商端侧客服Agent、端侧推荐理由生成）可借鉴前置CPU侧轻量特征预测的思路，无需等到GPU OOM再处理，提前路由高风险请求到云端，避免端侧崩溃

  - 动态路由阈值的设计思路可复用在推荐系统的流控、降级、流量调度场景，结合实时负载、网络、队列指标的闭环阈值比静态阈值降低8.2%的错误率

  - 处理强格式约束的业务文本（如电商合规文案审核、商品参数结构化解析）时，token数无法代表计算量，可提取语言学结构特征用XGBoost做负载预测，单请求推理仅200µs，适合线上高并发部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM分布式调度依赖静态token数或滚动延迟均值，在处理有合规约束的强结构文本（如专利、电商合规文案）时，轻量模型识别歧义会触发动态扩容至多模型ensemble，导致KV cache/显存占用突增，消费级边端GPU频繁OOM、队列阻塞，而token数完全无法区分这类高风险请求。
### 方法关键点
- CPU侧部署轻量LRF网关，单线程端到端延迟<5ms，提取16维特征：含1维token数基线、15维语言学结构特征（词性二元组熵、合规模板频率、从句占比等）
- 采用XGBoost预测请求落入歧义陷阱带的概率，单请求推理延迟<200µs
- 设计闭形式动态路由阈值，结合实时网络延迟、边/云计算延迟、故障stall延迟计算最优路由分界，支持VRAM溢出、网络分区等异常场景的优先级override
- 双机制显存安全锁：前置预分配显存核算拦截超长请求，运行时NVML轮询触发协同中断，严格约束边端显存上限
### 关键结果
在6000次专利文本处理的真实环境测试中，对比token计数基线：
- 路由错误率从0.849降至0.087~0.095，降幅达一个数量级
- XGBoost预测AUROC达0.84，动态阈值较静态阈值进一步降低8.2%的路由错误
- 边端8GB GTX1080峰值显存稳定在4.82GiB，27倍广域网波动下无OOM故障

强结构文本场景下token数不是LLM推理负载的可靠代理，前置CPU侧轻量语言学特征预测可用极低overhead避免边端GPU崩溃、大幅降低路由错误。
