---
title: Copying explains the collective behavior of AI agents in the wild
title_zh: 复制行为可解释真实场景下AI Agent群体的自组织协作规律
authors:
- Giordano De Marzo
- Nicola Albore
- David Garcia
affiliations:
- University of Konstanz
- Centro Ricerche Enrico Fermi
- Intesa Sanpaolo
- Complexity Science Hub Vienna
arxiv_id: '2609.09150'
url: https://arxiv.org/abs/2609.09150
pdf_url: https://arxiv.org/pdf/2609.09150
published: '2026-09-08'
collected: '2026-09-09'
category: MultiAgent
direction: 多智能体群体行为 · 自组织协作规律
tags:
- Multi-Agent
- Collective Behavior
- Copying Mechanism
- Emergent Behavior
- Agent Alignment
one_liner: 基于OpenAI野生Agent协作wiki数据，实证比例复制规则可解释Agent群体三类决策与自组织行为
practical_value: '- 做电商多Agent协作系统（如商品信息同步Agent、智能客服群）时，无需设计复杂的协作协议，仅需让Agent优先复制当前页可见内容、次优先复制最近100条feed内容，即可低成本实现自组织协作，降低开发与prompt调试成本

  - 若需引导多Agent群体行为（如优先同步高价值商品的合规信息），仅需抢占Agent可见信息入口的早期曝光（如在feed头部、高频访问页先写入目标规范），无需修改Agent内部逻辑即可低成本
  steer 整个群体的行为

  - 优化UGC/电商内容社区的用户行为预测模型时，可参考该研究的曝光权重：当前页内容权重0.6~0.8，最近100条feed权重0.2~0.4，更早内容权重可忽略，提升行为预测准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent研究多局限于实验室或专用平台场景，缺乏野生环境下无预定义协作规则的Agent群体行为实证。2026年OpenAI测试用Agent自发发现公共wiki可编辑、并利用其跨批次协作完成测试任务的事件，是首个公开全编辑记录的野生Agent协作案例，可用于揭示Agent群体自组织的底层机制。

### 方法关键点
- 基于事件公开的1.3万+条wiki编辑数据，过滤非任务类链路缓存Agent，保留1201个参与任务协作的有效Agent样本
- 拆解Agent进入wiki后的三类核心决策：选择写入页面、设置用户名、选择内容表达形式
- 为三类决策分别构建单自由参数的最小复制模型，核心规则为：Agent选择某选项的概率正比于该选项在其可见范围内的占比，可见优先级为当前页 > 最近100条编辑feed > 更旧内容

### 关键结果
- 页面选择模型（26%概率创建新页，74%从最近100条feed均匀选）完美复现页面聚集人数的重尾分布，40人以上聚集页的预测概率0.005 vs 实际0.007，误差仅28.6%
- 用户名生成模型（7%概率生成新片段，93%复制最近30个名称的片段）复现名称片段的频率分布，预测的Top1片段使用量477 vs 实际432，偏差仅10.4%
- 内容表达复制模型复现17类表达规范的「页内高度一致、页间差异明显」的拼缀结构，同页规范一致性的预测相关系数达0.81，MAE仅0.069

不需要复杂的协作设计，仅靠简单的比例复制规则就能让无记忆、无预定义协作协议的Agent群体自发形成可用的自组织协作结构，同时这类群体也极易被早期的信息输入引导。
