---
title: 'ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments'
title_zh: ProbeAgent：可验证环境下Agent故障的自动化诊断框架
authors:
- Yue Huang
- Yuchen Ma
- Shuhang Lin
- Yuyang Wu
- Zixuan Weng
- Zixiang Xu
- Xiangqi Wang
- Yuexing Hao
- Yujun Zhou
- Yue Zhao
affiliations:
- University of Notre Dame
- Ludwig-Maximilians-Universität München
- Rutgers University
- Carnegie Mellon University
- Georgia Institute of Technology
arxiv_id: '2611.26897'
url: https://arxiv.org/abs/2611.26897
pdf_url: https://arxiv.org/pdf/2611.26897
published: '2026-11-19'
collected: '2026-11-23'
category: Agent
direction: Agent 故障根因诊断与失效模式挖掘
tags:
- Agent Diagnosis
- Failure Mode Mining
- Automated Probing
- LLM Agent
- Root Cause Analysis
one_liner: 提出可验证环境下的Agent故障诊断框架，自动定位根因并生成共性失效模式描述
practical_value: '- 电商客服/导购/运营类Agent的故障排查可复用三重探针验证逻辑：先确认参考方案可过、空跑必败，再检查规则无漏洞，最后校验指令与实现一致，避免无效测试导致的故障误判

  - 要区分Agent偶发故障和固有缺陷时，可复用「保留触发条件、变更上下文生成兄弟任务」的复现测试方法，快速定位如「完成计算但不保存输出」这类跨场景共性问题

  - Agent故障聚类可复用带密度约束的语义聚类方案：基于故障原因、触发条件、修正动作做嵌入，要求组内平均相似度减去组外最大相似度高于阈值，比普通聚类准确率提升13个百分点以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent故障诊断仅能解释单次执行失败，无法区分是任务难度导致的偶发失败还是Agent固有行为缺陷，也不能自动聚合不同任务下的共性故障模式，手动排查效率极低，难以支撑业务级Agent的迭代优化。
### 方法关键点
- 三阶段诊断架构：
  1. 故障确认：从基准任务构建可执行探针，经过「参考方案执行通过/空操作执行失败+检查器规则校验+指令与实现一致性审核」三重验证后运行目标Agent，对失败轨迹自动生成包含错误动作、触发条件、修正方案的故障解释
  2. 故障复现验证：保留故障触发条件，更换任务领域、数据、输出格式生成兄弟任务，测试同一错误是否复现，将故障分为Agent固有缺陷、弱复现故障、任务特有一次性故障三类
  3. 失效模式发现：基于故障原因、触发条件、修正动作的语义嵌入计算相似度，加入「组内平均相似度 - 组外最大相似度 ≥ 阈值」的密度约束做聚类，为每类故障生成可区分其他相似错误的描述
### 关键实验
在22种Agent配置（15个主流LLM+7个Agent框架）、10个基准任务下测试，累计收集1244条可解释故障，生成536条失效模式描述；人类评估对故障描述的接受率达90.0%，相似错误的区分准确率达83.3%；加入密度约束后聚类描述的准确率从78.0%提升至91.8%；16.8%的故障被验证为Agent的固有行为缺陷，40.3%为任务特有的偶发故障。
### 核心结论
诊断Agent故障不能只看单次执行结果，通过可控变量的探针测试区分偶发错误和固有缺陷，才能真正有效指导Agent迭代。
