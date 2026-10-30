---
title: On the Fundamental Limits of Prefill-Based Decoding Length Prediction
title_zh: 基于Prefill阶段的LLM解码长度预测理论极限分析
authors:
- Haowen Shi
- Xuzhe Yan
- Fahao Chen
- Peng Li
affiliations:
- Xi'an Jiaotong University
- Shandong University
arxiv_id: '2610.40541'
url: https://arxiv.org/abs/2610.40541
pdf_url: https://arxiv.org/pdf/2610.40541
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: LLM推理调度 · 解码长度预测
tags:
- LLM_inference
- prefill
- decoding_length_prediction
- theoretical_bound
- scheduling
one_liner: 推导Prefill侧LLM解码长度预测的理论下界，验证主流预测器性能已接近天花板
practical_value: '- 搭建LLM推理服务（如电商客服Agent、生成式推荐内容生成服务）的解码长度预测模块时，直接选用简单的MLP-Concat架构即可，无需尝试EGTP、MoE等复杂设计，后者不会带来收益甚至会引入噪声导致精度下降

  - 做预测器性能评估时必须固定目标LLM、采样参数、测试数据集，优先报告相对误差指标（MAE/平均输出长度、实测acc@τ与理论天花板的比值），避免跨场景对比的指标失真

  - 若要提升调度效率，优先通过降低采样温度、增加解码约束、优化prompt等方式控制生成长度的方差，其收益远高于优化预测器架构；也可搭配每生成50-100token更新一次长度估计的迭代预测方案，进一步降低系统误差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM推理的Decode阶段占总时延和算力成本的主要部分，基于Prefill阶段信息预测解码长度是推理批量调度、资源分配的核心依赖，但现有基准测试结果极不稳定：相同预测器在不同模型、数据集、采样配置下MAE可能从80暴涨至260以上，核心原因未被厘清。
### 方法关键点
- 将自回归解码建模为带非恒定停止概率的随机过程，推导得到解码长度渐近服从正态分布，且满足σ=αμ+b的仿射方差定律，α为回答片段数的变异系数；
- 推导任意仅用Prefill信息的预测器的理论误差下界：MAE最小为σ√(2/π)≈0.8σ，给定容差τ的acc@τ存在不可突破的上限；
- 将总预测误差拆解为不可消除的系统误差（由生成过程固有随机性导致）和可优化的模型误差（由预测器拟合不足导致）。
### 关键结果
在ShareGPT 300条测试prompt（每条重复解码200次）、Qwen3-32B固定采样配置下测试8种预测器：
- 最简单的MLP-Concat取得最优MAE 168.1，仅比理论下界129.5高30%，EGTP、FiLM、MoE等复杂架构均未带来收益，EGTP甚至MAE飙升至466.8；
- Acc@100的理论天花板为57.9%，最优预测器仅达到48.9%，剩余差距来自训练标签噪声和分布偏移，与架构无关。
> 最值得记住的结论：Prefill侧解码长度预测的瓶颈是生成过程的固有随机性，而非预测器架构，优化优先级为「控生成方差>迭代预测>优化预测器设计」
