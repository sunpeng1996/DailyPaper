---
title: A Structured Debate-Mixture-of-Agents Framework for Complex Clinical Diagnostic
  Decision Support
title_zh: 面向复杂临床诊断决策支持的结构化辩论混合多Agent框架
authors:
- Chang Xia
- Leilei Ouyang
- Huimin Wang
- Yong Zhao
- Kang Li
affiliations:
- 四川大学计算机学院
- 四川大学华西医院华西生物医学大数据中心
- 四川大学Med-X信息中心
arxiv_id: '2609.05069'
url: https://arxiv.org/abs/2609.05069
pdf_url: https://arxiv.org/pdf/2609.05069
published: '2026-09-04'
collected: '2026-09-07'
category: MultiAgent
direction: 多智体结构化协作 · 复杂决策推理
tags:
- Multi-Agent
- Mixture-of-Agents
- Debate Framework
- LLM Reasoning
- Decision Support
one_liner: 提出带角色约束的辩论混合多Agent框架DMoA，大幅提升复杂临床诊断准确率与安全性
practical_value: '- 多Agent架构可复用：拆解为「生成-反驳-修订-聚合」的固定角色拓扑，效果优于无结构多轮对话或纯MoA方案，可迁移到复杂电商选品、投诉工单处理等高不确定性决策场景

  - 调优经验可借鉴：4×2的Agent规模（4个辩论单元，每个含1个生成+1个反驳角色）效果最优，无需盲目堆Agent数量；更大token预算可提升推理质量，信息拆分分发反而会降低效果

  - 小模型落地策略：全链路用同量级小模型搭建DMoA，效果显著优于同规模单模型，成本远低于大模型方案，适合C端高并发推荐/客服场景

  - 评估体系可参考：引入多维度安全+准确率双重评估，避免只看准确率忽略业务风险，可复用在广告文案生成、商品推荐的风控评估环节'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM单轮问答模式不符合临床诊断这类多步迭代的复杂决策逻辑，在罕见病、疑难病例等低确定性场景下准确率和安全性不足；现有多Agent方案多依赖无结构共识讨论，缺乏结构化协作推理流程，性能提升有限。

### 方法关键点
- 基于MoA框架扩展提出DMoA，采用固定角色拓扑：每个辩论单元含Presenter（生成初始诊断）和Rebutter（指出推理漏洞、缺失证据、备选诊断），Presenter根据反馈修订结果，最后由Aggregator整合所有辩论单元的修订结果输出最终结论
- 流程完全角色化，不强制Agent达成共识，保留多个冲突假设后再聚合，避免过早收敛到错误结论
- 支持轻量化部署，可搭配任意基座LLM，也支持混合模型配置

### 关键实验
在297例罕见病、1719例疑难病例数据集上测试，对比GPT-4o单模型基线，DMoA top1诊断准确率提升10.21个百分点，安全率提升11.36个百分点；消融实验证明性能提升并非来自更多模型或更长输出，而是结构化辩论流程；在简单临床知识问答场景下DMoA相比单模型无明显增益，仅在高复杂度决策场景发挥价值。

最值得记住的结论：多Agent协作的性能增益核心来自结构化的角色分工与流程设计，而非单纯增加Agent数量或用提示词模拟推理流程。
