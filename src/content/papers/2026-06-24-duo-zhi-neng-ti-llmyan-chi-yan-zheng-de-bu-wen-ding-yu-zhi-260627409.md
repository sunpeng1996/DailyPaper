---
title: 'Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds
  and Optimal Corrector Placement'
title_zh: 多智能体LLM延迟验证的不稳定阈值与校正器最优部署方法
authors:
- Igor Itkin
affiliations:
- Independent Researcher, Tel Aviv, Israel
arxiv_id: '2606.27409'
url: https://arxiv.org/abs/2606.27409
pdf_url: https://arxiv.org/pdf/2606.27409
published: '2026-06-24'
collected: '2026-07-01'
category: MultiAgent
direction: 多智能体协作 · 幻觉抑制稳定性优化
tags:
- Multi-Agent LLM
- Hallucination Mitigation
- Stability Analysis
- Corrector Placement
- Delay System
one_liner: 推导多智能体LLM验证延迟的稳定性阈值，给出有限校正器预算下的近似最优部署策略
practical_value: '- 部署多智能体客服、内容审核、投放效果预估系统时，避免验证延迟与通信延迟同步，延迟为2时验证增益不要超过逆黄金比≈0.618，防止共识震荡失效

  - 有限验证Agent预算下，直接复用论文给出的贪心算法，将校正器部署到网络桥节点、枢纽节点等高影响力位置，可获得1-1/e的最优近似效果，降低事实错误率

  - 数值类估算多智能体任务需严格控制验证增益、降低验证延迟，避免符号化误差震荡；基于RAG的grounded事实类任务几乎不受延迟震荡影响，可优先落地

  - 若观测到多智能体辩论出现结论反复横跳的退化现象，优先排查验证增益是否过高、延迟是否过大，无需先调整模型参数'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多智能体LLM系统普遍依赖验证Agent抑制幻觉，但验证过程天然存在延迟，期间错误声明会在网络中传播甚至放大，现有研究未考虑延迟对验证闭环稳定性的影响，也未给出验证强度、延迟与校正器部署的量化规则，无法解释多智能体辩论效果退化甚至不如单智能体的现象，亟需明确稳定性边界与可落地的优化方案。

### 方法关键点
- 将多智能体信念更新过程建模为带接地校正节点的图上延迟共识问题，通过grounded Laplacian谱分解将高维网络问题解耦为独立标量延迟递推问题，推导得到闭式稳定性阈值
- 校正器部署目标为超模函数，有限预算下用贪心算法选择边际增益最高的节点部署，可获得(1-1/e)的最优近似保证
- 推导通信延迟与验证延迟双耦合场景下的稳定区域，明确两类延迟同步是最不稳定的极端情况

### 关键结果
- 仿真实验中，非线性系统震荡起始点与理论阈值偏差仅约2%，匹配度极高
- 5款开源LLM的数值估算辩论实验中，不稳定场景（α=0.5、δ=6）下符号误差过零率达96%~100%，稳定场景（δ=1）下过零率仅0%~4%，阈值预测无拟合完全匹配
- grounded事实问答场景下延迟震荡完全消失，明确了不稳定现象仅存在于无约束符号信念任务的适用边界

### 核心结论
多智能体验证不是强度越高越好，存在最优验证剂量和部署位置，绑定约束是网络最慢的接地模态，可通过校正器部署放松约束。
