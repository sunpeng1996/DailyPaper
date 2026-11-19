---
title: 'Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity'
title_zh: 动态容量下LLM推理请求调度优化方案Cap-and-Track
authors:
- Benjamin Novotny
- Doug Szeto
- Chang Wang
- Shicheng Chen
- George Zhihua Yuan
- Bob Kamma
- Michael Ge
- John Xin Zhou
- Andrea Olgiati
affiliations:
- Meta
- Google
arxiv_id: '2611.24891'
url: https://arxiv.org/abs/2611.24891
pdf_url: https://arxiv.org/pdf/2611.24891
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM推理服务 · 动态容量调度
tags:
- LLM_inference
- dispatch_scheduling
- overload_control
- GPU_utilization
- production_deployment
one_liner: 基于拒绝信号自适应调整调度率，无需预测输出长度或手动调优固定速率
practical_value: '- LLM推理服务端开启单副本请求数上限（CAP），将引擎内排队溢出转为HTTP 429拒绝，避免goodput坍塌，无需修改推理引擎内核即可落地

  - 调度器采用MIMD策略，仅基于429拒绝率动态调整调度速率，无需预测输出长度、手动调优固定QPS，适配GPU集群弹性扩缩容、抢占、大促流量波动场景

  - 超出容量的请求存入外部持久化优先级队列，按业务优先级（如实时推荐请求>离线特征计算）调度，既保证高优请求时效，又提升GPU利用率

  - 集群sizing无需按峰值流量 provisioning，改为按低优先级任务容忍的等待时长配置，可节省30%+ GPU资源'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理调度依赖固定QPS配置，无法适配算力集群扩容/抢占、请求输出长度未知、流量潮汐/大促波动等动态场景，要么GPU闲置浪费，要么引擎排队过长导致超时goodput坍塌，手动调优效率极低，Meta内部原静态调度系统GPU batch填充率仅1/3，资源浪费严重。

### 方法关键点
- **CAP层**：在推理副本侧做快速拒绝检查，请求数超过预设阈值（略高于vLLM max_num_seqs）直接返回429，不进入引擎排队，避免请求在引擎内超时
- **TRACK调度器**：每15s统计429拒绝率，低于目标拒绝率（默认2%）则调度率升3%，高于目标分三档降速（<50%拒绝率乘0.99，50%-65%乘0.85，>65%乘0.5），自动跟随当前算力容量上限
- **架构配合**：超出容量请求存入外部持久化优先级队列，拒绝的请求返回本地队列头部无需重拉数据，调度状态集中管理避免多实例独立决策冲突

### 关键实验结果
- 生产A/B测试：分类任务同流量下比原静态调度少用43% H100，零样本任务同GPU规模下backlog排空速度快3小时，单GPU吞吐量高9%
- 稳态回放：TRACK goodput比最优固定调优速率低不到1%，拒绝率仅为固定速率的1/4
- 线上规模：承载每日3亿+在线请求，峰值24小时处理11亿请求，预留算力利用率达95.8%，满负载周利用率达99.1%

### 最值得记住的一句话
LLM推理调度可以类比网络拥塞控制，拒绝信号相当于丢包反馈，用轻量自适应策略替代复杂的容量预测和手动调优，投入极低收益极高
