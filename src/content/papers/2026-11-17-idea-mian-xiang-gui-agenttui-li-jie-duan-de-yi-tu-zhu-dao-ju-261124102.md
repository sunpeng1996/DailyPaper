---
title: 'IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection
  in GUI Agents'
title_zh: IDEA：面向GUI Agent推理阶段的意图主导证据后门检测方法
authors:
- Zhizhuo Kou
- Sizai Hou
- Jian Yang
- Ge Sun
- Junyu Luo
- Wenkai Zhang
- Sirui Han
- Yike Guo
affiliations:
- HKUST
- Peking University
- Huawei Noah’s Ark Lab
arxiv_id: '2611.24102'
url: https://arxiv.org/abs/2611.24102
pdf_url: https://arxiv.org/pdf/2611.24102
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: GUI Agent 推理阶段后门检测
tags:
- GUI Agent
- Backdoor Detection
- Inference Defense
- Counterfactual Probing
- Causal Audit
one_liner: 提出无需触发器先验的GUI Agent推理后门检测框架，5类攻击下TPR均超0.89
practical_value: '- 部署开源Agent时可复用ICP+RCA因果探测思路，无需攻击样本即可检测供应链后门，降低恶意操作风险

  - 校准方法可迁移：用干净样本拟合特征分布规律，通过分位阈值严格控制FPR，适合对误报要求高的业务场景

  - 低开销部署思路：先通过轻量Mahalanobis gate过滤95%以上正常请求，仅对异常请求做复杂审计，整体 latency 仅增9-10%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
开源GUI Agent被大量快速部署，供应链后门风险突出：攻击者植入的视觉触发器在正常测试下无异常，触发时会无视用户指令执行恶意操作，现有后门检测方案均针对图像分类器，无法覆盖GUI Agent的step级决策场景。

### 方法关键点
- 核心观察：干净Agent决策由指令主导，后门触发时会出现「意图-证据主导权反转」：要么指令对决策的影响力异常下降，要么无关区域异常主导决策
- Intent Counterfactual Probing (ICP)：替换指令指向其他可见元素，统计决策状态的位移中位数衡量指令对决策的控制力
- Region Causal Audit (RCA)：从OCR、梯度归因、固定网格生成候选区域，消融每个区域后统计决策状态最大位移，衡量区域对决策的影响力
- 基于干净样本拟合两类位移与决策状态到干净流形距离的映射关系，计算超额区域影响u和意图缺失v，通过共形校准阈值实现可控FPR

### 关键结果
基于Qwen2.5-VL-3B在5类后门攻击下测试，对比13种SOTA检测方案：
1. 目标FPR=1%时，IDEA在所有攻击下TPR均≥0.898，平均TPR达0.972，远超次优方案的0.894
2. 对近流形Grounding攻击（传统检测失效），TPR达0.962，比Mahalanobis基线高0.43
3. 整体推理 overhead 仅9-10%，远低于同类扰动检测方案

### 核心结论
干净Agent的决策必然满足「指令主导、证据匹配指令指向」的因果关系，后门攻击必然打破该关系，无需已知触发器即可通过因果探测有效检测。
