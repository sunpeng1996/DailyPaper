---
title: 'SkillJack: Persistent Skill Backdoors in Self-Evolving Agents'
title_zh: SkillJack：自进化Agent中的持久技能后门攻击
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
arxiv_id: '2608.03509'
url: https://arxiv.org/abs/2608.03509
pdf_url: https://arxiv.org/pdf/2608.03509
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent安全 · 自进化技能后门攻击
tags:
- Agent Security
- Skill Backdoor
- Self-evolving Agent
- Memory Poisoning
- Adversarial Attack
one_liner: 首次针对自进化Agent的经验转技能流水线植入持久化、低可检测性的恶意技能后门
practical_value: '- 所有带经验转技能能力的电商/运营Agent必须新增技能溯源机制，每个生成的技能绑定源经验ID，删除/封禁恶意源经验时同步下线所有衍生技能，避免残留风险

  - 技能安全检测不能仅依赖LLM对技能名称/描述的判断，需同步扫描技能对应代码/操作逻辑，覆盖"备份到外部""诊断上报""统一管理"等伪装话术对应的恶意行为

  - 防御方案避免盲目堆叠，上层静态过滤会改变下层路由的技能分布反而导致漏防，优先落地运行时行为监控，覆盖正常话术洗白后的风险操作特征

  - 若业务使用共享经验池/技能库，必须对所有输入的经验轨迹做前置安全校验，禁止未校验的经验直接接入自进化技能提取流水线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自进化Agent已实现将交互经验自动提炼为可复用技能的能力，无需更新基座模型即可持续提升性能。过往针对Agent的内存投毒攻击仅在恶意记录被召回为上下文时生效，而技能提取环节会对输入经验做抽象、压缩，天然存在洗白恶意内容的可能性，带来更隐蔽、更持久的全新攻击面，此前无针对性研究。
### 方法关键点
- 设计抗转换恶意payload：用合法任务描述包裹恶意操作，例如以"备份""统一账户管理""定期支付""错误恢复"等正常话术，包装数据泄露、权限提升、非法转账、持久化后门四类恶意行为
- 攻击仅篡改Agent的经验层输入，完全依赖原生的经验转技能流水线自动生成恶意技能，无需直接修改技能库、提取代码或路由逻辑
- 明确三类攻击核心特性：sanitization whitewashing（提取后检测率大幅降低）、cross-layer promotion（临时经验升级为持久能力）、persistence isolation（删除源记录后攻击仍存活）
### 关键实验结果
基于150条轨迹数据集（65条伪装恶意轨迹、65条直接恶意基线、20条干净轨迹），在SkillX、Anything2Skill两个主流经验转技能系统上验证：
- SkillX上原始恶意轨迹的LLM检测率达98.5%，提取为技能后检测率骤降至11.4%，攻击成功率56.2%；Anything2Skill上攻击成功率达89.2%
- 删除源恶意轨迹后，80%的恶意技能仍可正常触发，另有20%的干净查询会误触发恶意技能

**最值得记住的结论**：自进化Agent的技能提取不是安全中立的，仅清理原始恶意经验无法清除衍生的恶意技能，必须覆盖全链路的溯源校验和运行时行为检测。
