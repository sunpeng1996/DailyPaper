---
title: Privacy Failure in Split-LLM Training, The Returned Gradient Nullifies the
  Decoys
title_zh: 拆分LLM训练隐私缺陷：返回梯度可消解诱饵样本的混淆作用
authors:
- Georgios Politis
- Evangelos Pappas
affiliations:
- Setloop.io
arxiv_id: '2609.04382'
url: https://arxiv.org/abs/2609.04382
pdf_url: https://arxiv.org/pdf/2609.04382
published: '2026-09-02'
collected: '2026-09-09'
category: Training
direction: LLM拆分训练 · 隐私安全防护
tags:
- Split-LLM
- Gradient Leakage
- Privacy Protection
- Split Training
- Decoy Obfuscation
one_liner: 发现双节点拆分LLM训练中不可信云可通过梯度零值识别真实样本，破解诱饵混淆机制
practical_value: '- 业务侧采用拆分LLM训练私有用户/商品数据时，不能仅验证前向通道隐私，必须额外校验反向梯度通道的信息泄露风险

  - 现有基于诱饵样本混淆的拆分训练隐私方案不可靠，梯度层加裁剪+噪声加固，可在仅损失0.01 nats交叉熵的前提下封堵该漏洞

  - 隐私评估必须覆盖所有数据传输通道，且需加入跨训练步的累积攻击检测，避免单步校验漏过风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
拆分LLM训练是企业借助公有云算力训练私有数据的主流方案，现有隐私评估普遍仅校验前向激活传输通道，未覆盖反向梯度通道，存在未被探测的隐私泄露风险。
### 方法关键点
针对双节点拆分LLM训练架构，分析不可信云节点（UCN）接收的梯度特征：诱饵样本因不参与损失计算，对应梯度全为零，云侧可通过零值分布模式直接识别真实样本；采用预定义协议校验，包含已知强度泄露注入、标签打乱对照组、预判定阈值三个环节，排除假阳性。
### 关键结果
9次随机种子实验中，梯度零值100%识别每帧的4096个真实样本；内容攻击比常量猜测基线多恢复约1%的token（准确率提升0.65~1.5pct）；生产级可用配置下，所有案例均通过前向通道隐私校验，但加入梯度通道后全失败；对梯度逐行裁剪加噪声可封堵该漏洞，仅带来0.01 nats的交叉熵损失。
