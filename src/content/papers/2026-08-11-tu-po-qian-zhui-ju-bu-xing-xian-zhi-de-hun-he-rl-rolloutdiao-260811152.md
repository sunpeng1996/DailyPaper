---
title: Scheduling Mixed RL Rollouts Beyond Prefix Locality
title_zh: 突破前缀局部性限制的混合RL Rollout调度策略MISA-T
authors:
- Zetao Hong
- Song Yuan
- Yuanhao Ding
- Yibo Zhu
- Daxin Jiang
- Zhibin Wang
- Chen Tian
affiliations:
- Nanjing University
- StepFun
arxiv_id: '2608.11152'
url: https://arxiv.org/abs/2608.11152
pdf_url: https://arxiv.org/pdf/2608.11152
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM推理调度 · KV cache优化
tags:
- KV_cache
- LLM_serving
- RLHF
- Scheduling
- Rollout
one_liner: 提出混合RL Rollout场景路由层准入策略MISA-T，大幅提升吞吐量同时保障训练任务配比
practical_value: '- 做Agent推理服务的团队可直接复用MISA-T的准入控制逻辑，给不同类型请求（工具调用/长上下文推理/普通问答）分配独立KV配额，避免单类请求打满缓存导致前缀命中率暴跌

  - 开展LLM RLHF/RLVR训练的团队可用MISA-T替代vLLM原生路由，无需反复调优静态并发阈值，即可提升30%+的Rollout吞吐量，缩短训练迭代周期

  - 混合负载的LLM服务可参考按请求类型+KV滞留时间加权分配容量的思路，比全局统一准入控制的缓存稳定性和吞吐量表现高20%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM RL后训练阶段常混合RLVR、RLHF、Agent三类Rollout请求，现有前缀感知路由仅做实例选址不做准入控制，高并发下不同请求的KV footprint、滞留时间差异极大，易触发缓存频繁驱逐、前缀命中率暴跌的正反馈循环，不仅导致吞吐量骤降，还会打乱训练侧指定的任务配比，影响训练效果。
### 方法关键点
- 自适应会话准入：根据实时KV负载、前缀命中率动态调整实例的全局会话上限，超过上限的新会话暂时HOLD等待，保护已有会话的缓存不被驱逐，无需反复调优静态并发阈值
- workload感知容量分配：按不同请求类的KV footprint需求划分独立准入配额，避免单类请求占用全部缓存，同时保证训练侧指定的任务配比不受调度层影响
- 滞留时间感知KV核算：将不同请求的KV滞留时间（含Agent工具调用间隔的缓存持有时间）纳入配额计算，按块时间需求加权分配容量，更贴合真实资源占用
### 关键实验
在Step3.7 196B MoE和Qwen3.6-35B两个模型上对比经参数扫描调优的vLLM Router基线：
- 纯Rollout推理场景下，MISA-T分别提升Rollout吞吐量53.3%、43.6%，前缀命中率稳定在95%以上
- 端到端50轮Step3.7训练场景下，提升Rollout吞吐量35.6%，平均迭代时间缩短22.8%，任务配比偏差从4.14个百分点降至2.71个百分点，下游任务得分无明显下降
### 核心结论
混合负载下的LLM调度不能只优化前缀选址，准入控制层面按请求特征分配KV容量是避免缓存雪崩、提升吞吐量的核心手段
