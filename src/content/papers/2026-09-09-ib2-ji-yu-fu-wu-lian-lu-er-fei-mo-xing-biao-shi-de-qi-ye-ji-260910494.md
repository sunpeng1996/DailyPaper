---
title: 'IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not
  Model Identifier'
title_zh: 《IB2：基于服务链路而非模型标识的企业级AI系统评估协议》
authors:
- Blake Stenstrom
- Charangan Vasantharajan
- Brian Sathianathan
affiliations:
- Iterate.ai
arxiv_id: '2609.10494'
url: https://arxiv.org/abs/2609.10494
pdf_url: https://arxiv.org/pdf/2609.10494
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: 企业级AI系统评估协议设计
tags:
- Evaluation
- Enterprise AI
- Serving System
- Benchmark
- Protocol
one_liner: 提出IB2评估协议，基于服务链路而非模型标识量化企业AI系统实际可用能力
practical_value: '- 选型线上LLM/Agent服务时，不要仅参考宣传的模型标识，需覆盖服务路由、工具调用解析、精度配置等全链路实际表现，避免选型偏差

  - 搭建内部AI服务评估流程时，可复用gold-blind预校验机制，先验证链路是否满足任务执行合约再跑正式测试，降低无效评估成本

  - 统计推荐/Agent线上效果时，不要直接剔除失败请求，需将可靠性纳入最终得分，避免评估结论与实际业务表现脱节'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有18个公开AI基准仅基于模型标识打分，但企业部署的AI系统实际可用能力由权重、serving链路、精度、输出合约、harness共同决定，存在严重测量误差。
### 方法关键点
IB2协议包含三个核心模块：
1. gold-blind能力绑定预校验：任务下发前先验证链路能否满足评估合约
2. 含可靠性的首过评分规则：将失败请求计入得分、排除不支持的能力项
3. 结构上的评分盲态裁决机制
### 关键结果数字
对11个系统测试得到核心结论：
1. 同权重下不同服务链路的预校验通过率存在差异，模型标识无法反映能力边界
2. 7个测试套件中4个在6个系统区间内饱和，区分度主要来自数据库操作、多表关联任务
3. 服务链路选择可让同模型精度得分从77.38提升至82.54，提升区间为[0.11,10.60]
4. 剔除失败请求会改变系统排名，纳入可靠性会直接修正评估结论
