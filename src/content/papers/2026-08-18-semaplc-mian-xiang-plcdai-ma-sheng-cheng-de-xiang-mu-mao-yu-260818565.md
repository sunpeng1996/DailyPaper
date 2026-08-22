---
title: 'SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code
  Generation'
title_zh: SemaPLC：面向PLC代码生成的项目锚定与验证门控Agent框架
authors:
- Yanlun Tu
- Huacan Wang
- Ziyue Zhou
- Jie Zhou
- Ningyan Zhu
- Ge Chen
- Wangyi Chen
- Tengfei Zhou
- Yifan Zhou
- Dasheng Yang
affiliations:
- Midea AIRC
- KUKA
- SJTU
- ZJU
arxiv_id: '2608.18565'
url: https://arxiv.org/abs/2608.18565
pdf_url: https://arxiv.org/pdf/2608.18565
published: '2026-08-18'
collected: '2026-08-22'
category: Agent
direction: Agent 代码生成校验框架
tags:
- Agent
- Code Generation
- LLM
- Verification
- Industrial AI
one_liner: 提出带三重外部校验机制的Agent框架，大幅提升PLC生成代码的编译、静态及动态运行通过率
practical_value: '- 可复用「外部校验门控终止逻辑」替代LLM自判断停止机制，应用于Agent生成物料（文案、营销素材等）的合规性校验链路，提升生成内容可用性

  - 可借鉴「项目上下文锚定」设计，在多模块联动生成场景（如电商活动页全链路内容生成）提前对齐现有项目约束，减少上下文冲突

  - 动态运行时校验思路可迁移到推荐/广告策略上线前的小流量验证环节，替代纯静态指标评估，更准确衡量生成内容/策略的真实业务效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM生成PLC代码仅支持独立程序单元生成，生成结果与现有项目的兼容性、运行正确性缺乏完整校验流程，依赖模型自评估的停止规则可靠性极低。

### 方法关键点
1. 项目锚定模块提前抽取现有PLC项目的结构、接口、IO映射等上下文，前置对齐生成约束；
2. 验证门控替代LLM自判断停止逻辑，仅生成结果通过规格校验、编译校验、实时运行行为三层外部校验才判定任务完成；
3. 动态行为校验通过对比生成代码与参考代码在真实PLC runtime的执行Trace，保证运行一致性。

### 关键结果
- 117个独立POU任务上，7个测试模型的平均严格验证通过率达72.6%，为当前最优；
- 65个项目上下文任务中，动态行为得分达52.2，远超基线的22.4~31.4，全层指标均显著优于基线。
