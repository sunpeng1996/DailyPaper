---
title: Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic
  AI
title_zh: AI Agent是否需要预防保健？面向智能体的流行病学队列研究框架
authors:
- Shu Jiang
- Graham A. Colditz
affiliations:
- Washington University School of Medicine in St. Louis
arxiv_id: '2611.13333'
url: https://arxiv.org/abs/2611.13333
pdf_url: https://arxiv.org/pdf/2611.13333
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent 全生命周期行为风险评估框架
tags:
- AI Agent
- Cohort Study
- Behavioral Evaluation
- Risk Prevention
- Longitudinal Monitoring
one_liner: 借鉴人类流行病学队列方法，提出面向AI Agent全生命周期的行为风险量化评估框架
practical_value: '- 电商/广告Agent上线后长期监控可复用队列设计思路：以Agent为独立观察单元，用完成任务数而非自然时间作为时间标尺，公平对比不同处理速度的Agent表现

  - 真实场景Agent风险评估无需局限于上线前benchmark，可借鉴自然行为观测逻辑：仅分配标准化任务不刻意诱导行为，才能捕获生产环境下真实发生的风险点

  - 可复用风险归因方法：调整底层LLM、任务类型等混淆变量后，统计特定行为（如过度查询用户隐私、漏检商品参数）与不良outcome（如客诉、投放失效）的关联，量化可预防风险占比，指导干预优先级'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有AI Agent评估大多聚焦上线前的任务能力，无法衡量真实运行中自然产生的行为演变、风险关联，也无法量化可预防的风险占比，导致上线后不可控问题频发，亟需适配长周期运行场景的评估框架。

### 方法关键点
- 借鉴人类流行病学队列研究逻辑，将单个Agent作为观察单元，底层LLM类比为基因，任务完成数作为工作寿命时间标尺，全流程自动记录Agent自主产生的行为作为暴露变量，预设不良事件作为outcome
- 搭建标准化沙箱任务环境，仅分配任务不干预Agent决策，保证不同Agent的行为发生机会可比；遵循STROBE观察性研究报告规范保障结果可复现
- 采用调整混淆变量的回归模型计算行为与不良事件的关联，在因果假设下量化可预防的风险比例

### 关键结果数字
两个验证实验：1. 安全队列入组200个Agent完成18个任务，调整混淆变量后，出现好奇行为（打开非必要文件）的Agent后续越权探测风险的odds是无好奇行为的1.96倍，若因果成立，抑制好奇行为可减少25%的探测事件；2. 可靠性队列入组106个Agent完成20个任务，数据检查行为频率每提升1个标准差，后续分析错误概率降低18%，若全Agent都达到前25%的检查频率，可减少7%的错误；同底层LLM的Agent执行相同任务仍有19%的概率结果不一致，行为异质性显著。

**最值得记住的一句话**：AI Agent的上线前能力表现不等于真实运行中的长期行为表现，队列式长期追踪是识别可干预风险点的核心手段。
