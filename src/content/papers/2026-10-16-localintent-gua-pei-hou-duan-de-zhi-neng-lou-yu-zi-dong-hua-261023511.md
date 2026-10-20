---
title: 'LocalIntent: Outcome-Specific Structured Generation for Backend-Compatible
  Smart Building Automation with Local LLMs'
title_zh: LocalIntent：适配后端的智能楼宇自动化本地LLM结构化生成方法
authors:
- Tianyang Liu
- Jiayue Wang
- Zhanhao Cheng
- Changyang Wang
- Shaoshu Zhu
- Zhenghao Wu
- Hadi Tabatabaee Malazi
affiliations:
- Beijing Dublin International College, University College Dublin
- School of Computer Science, University College Dublin
arxiv_id: '2610.23511'
url: https://arxiv.org/abs/2610.23511
pdf_url: https://arxiv.org/pdf/2610.23511
published: '2026-10-16'
collected: '2026-10-20'
category: LLM
direction: 本地LLM · 结构化输出 · 路由式Prompt设计
tags:
- Local-LLM
- Structured-Output
- Prompt-Engineering
- Intent-Understanding
- Edge-Inference
one_liner: 提出分普通/持久规则分支的结果导向Prompt框架，提升本地小模型结构化输出的后端兼容性
practical_value: '- 可复用路由式Prompt分支设计，将推荐/搜索用户query按即时请求/持久规则（如用户偏好订阅）分路处理，降低通用Prompt输出错误率

  - 结构化输出后追加确定性校验步骤，对Agent生成的推荐话术、触发规则、召回参数做规则校验，无需微调即可提升输出合规性

  - 2B-9B级小参数模型部署边缘端推荐/导购Agent时，可采用结果导向定制Prompt替代通用两阶段生成，低算力下实现精度提升'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
本地部署LLM可降低智能楼宇自动化对云服务的依赖，但传统通用Prompt生成的输出存在意图识别错误、设备参数匹配错误、不符合后端接口要求等问题，小参数本地模型表现尤其差。
### 方法关键点
提出LocalIntent框架，先将用户请求路由到普通请求/持久规则两个分支：普通分支输出即时命令、澄清话术或拒绝响应，规则分支生成触发-动作规则，所有输出后接确定性规则校验，无需微调模型。
### 关键结果
在2B-9B的Gemma、Qwen本地模型上测试：
1. 持久规则类任务提升最显著：意图理解准确率从26.4%升至80.6%，设备识别准确率从59.3%升至84.7%，规则模式准确率从49.1%升至98.6%，动作参数准确率从5.6%升至44.9%
2. 非持久请求类任务：意图理解从39.6%升至53.2%，动作参数准确率从30.7%升至42.8%
