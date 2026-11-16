---
title: 'VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling'
title_zh: VelServe：基于尾部校准调度的LLM推理解码抖动优化
authors:
- Ishaan Datta
- Alind Khare
- Koushik Kumar Dey
- Ratnesh Jamidar
- Anand Kumar Singh
affiliations:
- Sprinklr
- Microsoft
arxiv_id: '2611.18392'
url: https://arxiv.org/abs/2611.18392
pdf_url: https://arxiv.org/pdf/2611.18392
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM 推理调度 · SLO 优化
tags:
- LLM_serving
- inference_scheduling
- SLO_optimization
- decode_jitter
- tail_latency
one_liner: 提出尾部校准的LLM推理调度器，聚合/拆分部署下均大幅提升SLO达标吞吐量
practical_value: '- 业务中使用LLM做Agent对话、生成式推荐文案、语义搜索query补全等需要流式输出的场景，可直接复用尾部校准预算逻辑，基于线上实际迭代延迟的残差分布预留headroom，避免解码抖动导致的输出卡顿、用户体验下降

  - 调度排序可直接复用「短prompt优先+长度感知TTFT deadline」策略，缓解长prompt（如商品详情生成、多轮Agent上下文处理）阻塞短请求的问题，提升电商搜索query、用户即时提问等短请求的响应速度

  - 多GPU拆分prefill/decode的部署架构下，可借鉴批量准入逻辑，对齐所有GPU的新请求准入时机、控制准入频率，降低join抖动对TBT的影响，提升长流式输出的体验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
交互式LLM服务（如Agent多轮对话、流式生成式推荐文案、智能客服）需要严格满足首token延迟（TTFT）和token间隔（TBT）的SLO，现有调度方案要么使用静态token预算导致长prompt阻塞短请求的队头问题，要么把每轮迭代填到预测延迟上限，没有预留容错空间，即使仅1%的解码抖动也会因长输出跨数百步的放大效应导致大量SLO违约，拆分prefill/decode的部署架构下新请求加入解码批次的抖动也会触发同类问题。
### 方法关键点
- 尾部校准token预算：基于线上最近迭代的延迟残差分布计算headroom，确保迭代预测延迟+headroom低于TBT目标，把抖动概率控制在SLO允许范围内
- 最短剩余prompt优先调度：长prompt的TTFT deadline随长度线性增长，短请求优先调度不影响长请求SLO达标率，从根源缓解队头阻塞
- 拆分部署批量准入：对齐所有GPU的新请求准入时机，控制准入频率，把每个请求遇到的join抖动次数控制在P99 TBT允许范围内
### 关键实验
覆盖GQA、MLA、压缩注意力三类架构的Qwen3-8B、DeepSeek-V2-Lite、DeepSeek-V4-Flash模型，对比vLLM、Sarathi、Medha、Niyama等主流调度器，聚合部署下SLO goodput是最优基线的2.4~4.4倍；8GPU拆分prefill/decode部署下，SLO达标请求数是基线的2倍以上。
### 核心结论
解码抖动的放大效应远高于直觉，即使1%的单步抖动也会导致95%的300-token输出请求遇到至少一次延迟，预留tail-calibrated的headroom比精确预测单步延迟更重要
