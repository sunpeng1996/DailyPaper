---
title: 'Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts'
title_zh: 反事实引导的智能体Harness进化框架：规避基准级捷径作弊
authors:
- Guojun Zhu
- Xunheng Huang
- Peng Yin
- Jiahui Xie
- Sanguo Zhang
- Doudou Zhou
affiliations:
- University of Chinese Academy of Sciences
- National University of Singapore
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2609.18366'
url: https://arxiv.org/abs/2609.18366
pdf_url: https://arxiv.org/pdf/2609.18366
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent 鲁棒性评估与Harness优化
tags:
- Agent-Evaluation
- Harness-Optimization
- Counterfactual
- Shortcut-Mitigation
- Benchmark-Robustness
one_liner: 提出CHASE框架，通过反事实基准变换抑制Harness优化中的基准级捷径，提升泛化能力
practical_value: '- 做电商导购/客服/RAG检索类Agent的Harness优化时，可复用CHASE的反事实校验机制，避免优化出的Prompt/检索逻辑仅适配测试集固定目录、文件命名等表层捷径，上线后泛化失效

  - 推荐系统离线Benchmark设计可借鉴协议变换思路，在保留用户/Item语义的前提下变换特征编码、排序规则的表层形式，避免模型学到离线Benchmark特有捷径导致上线掉点

  - 业务算法评估可拆分进化集、发现集、确认集、认证集四类完全互斥的任务集，确保优化方案的效果不是靠数据泄露或捷径得到，提升评估可靠性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有Agent的Harness（包含Prompt、记忆规则、检索逻辑、工具调用规则、输出处理逻辑的可执行上下文）优化过程中，会学到两类捷径：任务级捷径（匹配任务ID直接返回答案）和基准级捷径（利用基准固定的目录结构、文档排布、证据位置等全局表层关联提分）。仅靠任务留验的传统评估方法只能识别任务级捷径，无法发现基准级捷径，导致优化后的Harness在真实场景泛化性极差，上线后效果大幅下跌。
### 方法关键点
- 交替运行Proposer与Challenger双模块：Proposer迭代优化Harness提升发布基准得分，Challenger生成保持任务语义的基准协议反事实变换（如打乱文档的检索通道分布、调整表格与上下文的相对位置）
- 设计有效性防火墙校验变换的语义一致性，通过独立确认集验证变换是否能大幅破坏当前Harness的增益，符合要求的变换加入约束档案，后续Harness优化必须满足所有档案约束
- 提供严格统计保证：有限反事实档案的约束可覆盖基准级捷径的中性化要求，搜索过程可在有限轮次后达到无明显可利用捷径的状态
### 关键结果
在OfficeQA政务文档问答基准、Syn-Ledger合成账本基准上测试，对比RawHarness、HarnessCompass基线：OfficeQA上CHASE发布协议得分68.86%，比基线高0.88~4.82pct；跨协议平均得分68.42%，最坏情况得分67.98%，波动仅0.88pct；跨 corpus 的Pro V2得分30.37%，比基线高4.07~4.34pct。
### 核心结论
仅靠任务留验无法评估算法鲁棒性，保持语义的协议级反事实变换是识别基准级捷径、提升方案泛化性的核心有效手段
