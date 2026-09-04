---
title: 'SciLENS: RL-Driven Autonomous Agents for Scientific Localized Evidence Navigation
  and Synthesis'
title_zh: SciLENS：RL驱动的全本地化科研证据导航与合成自主Agent
authors:
- Leqi Zheng
- Jinbo Su
- Yuying Li
- Chaokun Wang
- Weiping Wang
- Haitao Li
- Jiajun Zhang
- Shannan Yan
- Zhaolu Kang
- Rong Fu
affiliations:
- Tsinghua University
- Renmin University of China
- Institute of Information Engineering, CAS
- USTC
- Peking University
arxiv_id: '2609.03338'
url: https://arxiv.org/abs/2609.03338
pdf_url: https://arxiv.org/pdf/2609.03338
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 自主Agent · 本地化工具链 RL 对齐
tags:
- Agent
- RLHF
- Local-Deployment
- Tool-Use
- Synthetic-Data
one_liner: 全本地化RL驱动科研Agent，集成可视化工具链，性能比肩前沿闭源模型
practical_value: '- 本地化双轨存储架构（MongoDB + 分布式FAISS）可直接复用在电商全域商品/内容检索场景，千万级索引实现亚秒级访问，规避外部API依赖的稳定性问题

  - 反向分解评分+多维度RL奖励设计可迁移到推荐Agent的工具调用对齐，除最终结果奖励外额外叠加规划步骤、证据归因的细粒度奖励，大幅降低幻觉

  - 无人工标注的自动数据合成流程，基于知识图谱随机游走+多模型交叉验证生成训练样本，可复用在电商/广告场景多跳推理Agent训练，降低标注成本

  - Agent推理链路内置可视化工具的设计思路，可用于生成电商大促/类目趋势多模态分析报告，压缩高维用户/交易拓扑降低上下文开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有科研Agent三类范式均存在核心缺陷：标准RAG缺乏多跳推理能力，网络搜索Agent依赖外部API稳定性差、数据不可控，深度研究Agent纯文本推理易出现上下文溢出、幻觉严重，且训练依赖昂贵的人工标注，开源方案性能远低于闭源模型，无法满足大规模文献合成需求。

### 方法关键点
- 架构：全本地化双层存储架构，MongoDB存储元数据+分布式FAISS做向量检索，索引1200万学术记录，实现亚秒级响应
- 工具链：首次将结构化可视化工具纳入Agent推理循环，内置12种工具覆盖语义检索、引文拓扑遍历、图表生成、文本摘要，自动压缩高维拓扑降低上下文开销
- 训练：无标注数据合成流程，从引文知识图谱随机游走抽取子图，20个前沿模型交叉验证生成多跳QA对；两阶段训练：SFT蒸馏教师模型工具调用轨迹（屏蔽观测损失避免干扰），再用反向分解评分的RL对齐，叠加格式合规、答案正确性、规划合理性、证据归因多维度奖励

### 关键结果
在6个科研基准测试，所有模型使用统一本地工具链无网络访问：SciLENS-RL超过所有开源基线，性能比肩GPT-5.2、Gemini-3.0-pro：SSB结构合成基准得分0.7607，SciFR事实推理基准得分0.7594，SciFact准确率88.94%，引文准确率83.72%。

**最值得记住的一句话**：将可视化作为推理工具纳入Agent循环、搭配细粒度过程奖励的RL对齐，是本地化Agent赶超闭源模型的可行路径
