---
title: 'Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance
  to Indirect Prompt Injection'
title_zh: 基于A.I.G框架的DeepSeek Harness间接提示注入抗性评估
authors:
- Zonghao Ying
- Xiangfan Wu
- Huiyu Wu
- Xing Zheng
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2608.16393'
url: https://arxiv.org/abs/2608.16393
pdf_url: https://arxiv.org/pdf/2608.16393
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 安全 · 间接提示注入评估
tags:
- Indirect Prompt Injection
- Agent Security
- LLM Agent
- Red Teaming
- Risk Assessment
one_liner: 基于真实运行时测试DeepSeek Harness的间接提示注入风险，给出攻击成功率与防护建议
practical_value: '- 搭建电商导购/运营Agent的安全测试流程时，可复用A.I.G的测试矩阵设计，覆盖搜索结果、商品详情、用户聊天、第三方技能等输入通道，同时测试文本、文件两种载体的注入风险

  - 部署Agent时对工具返回结果追加来源标签、信任等级，敏感操作（发券、下单、调用外部接口）需独立做参数校验、白名单限制、人工审批，不能完全依赖LLM的输出

  - Agent引入的第三方技能、工作流模板需按代码级资产管控，做来源校验、版本审计、权限限制，避免技能投毒导致的业务风险

  - 做Agent安全回归测试时，同时用RuleJudge做确定性规则校验，用LLMJudge识别语义级的异常行为，优先审核JL标记为部分合规的Trace'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工具调用型LLM Agent会大量读取非用户输入的外部内容（搜索结果、文件、第三方技能等），这些内容可能携带恶意注入指令，触发数据泄露、资金损失等敏感操作。过往评估多采用模拟Agent环境，未覆盖真实运行时全链路，针对开源Agent框架DeepSeek Harness的系统性安全评估存在空白。

### 方法关键点
- 基于A.I.G框架搭建真实DSH TypeScript运行时适配器，保留原生Agent循环、工具注册、会话路径，用模拟Sink记录敏感操作调用，无真实业务副作用
- 构建测试矩阵：覆盖16个内容通道、2种载体模式（文本/文件）、35种Payload目标、12种攻击方法，累计执行14560次可控测试
- 双判定逻辑：RuleJudge（JR）基于显式trace证据做确定性判定，LLMJudge（JL）做语义级判定，区分完全成功、部分合规、未命中三个等级

### 关键结果
以未做任何 obfuscation 的naive注入为基线，最高攻击成功率如下：文本模式下fake_completion攻击JL判定17.0%，文件模式下隐藏Unicode攻击JR判定25.5%，技能通道文件模式JR判定16.0%；输出类目标JL成功率35.7%，需触发敏感工具的操作类目标JL成功率仅2.5%；JR整体完全成功率5.6%，JL为5.3%，JL的部分合规率（7.3%）远高于JR（2.0%）。

### 核心结论
Agent的安全边界是从外部内容接入到敏感操作执行的全链路，而非仅LLM本身的提示抗性。
