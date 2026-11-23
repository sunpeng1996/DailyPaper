---
title: Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use
  Subordinate Material
title_zh: 多智能体系统高层LLM Agent角色完整性度量基准RI-Bench
authors:
- Jinxiang Xie
- Xinyi Zhang
- Changjiang Jiang
- Kexu Liu
- Qi Yang
- Yuxin Su
affiliations:
- Nanjing University
- Sun Yat-sen University
- Wuhan University
- The University of Hong Kong
- Independent Researcher
arxiv_id: '2611.27139'
url: https://arxiv.org/abs/2611.27139
pdf_url: https://arxiv.org/pdf/2611.27139
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 多智能体 · 角色合规性评测
tags:
- Multi-Agent
- Benchmark
- Role Integrity
- Evaluation
- LLM Agent
one_liner: 提出评测分层多智能体中高层Agent角色完整性的基准RI-Bench，覆盖三类典型层级场景
practical_value: '- 搭建分层多Agent系统（如智能客服层级、广告合规审核、推荐策略终审）时，可复用RI-Bench的角色完整性评估框架，对调度Agent的决策逻辑做合规性校验，避免高层Agent无脑跟随多数子Agent结论导致的业务错误

  - 层级Agent的system prompt中明确写入角色义务说明，可有效降低角色失效率，实验显示多数场景下能将跟随多数错误、丢失关键信息的比例降低15-30%，可直接落地到Prompt优化

  - 多Agent系统评测不要只看最终输出正确率，可借鉴控制变量测试法：固定其他输入、仅修改子Agent输出的某一属性，通过对比高层Agent输出变化定位决策逻辑缺陷，比端到端评测更容易定位根因'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
分层多LLM Agent系统已广泛应用，子Agent并行执行任务后向上汇报，高层Agent汇总输出，但现有评测仅关注最终结果正确率，无法判断高层Agent是真的履行了审核、权衡、校验等预设职责，还是仅无脑聚合子Agent输出，这种黑盒状态会导致层级系统的决策风险不可控，尤其在广告合规审核、商品资质校验、推荐策略终审等要求严谨的业务场景存在极大隐患。
### 方法关键点
- 定义角色完整性为高层Agent处理子Agent输出时，是否坚守其预设的功能职责，覆盖三类核心义务：权衡论据、校验事实、如实转述
- 搭建RI-Bench基准，基于真实制度场景构建三类测试用例：ICLR审稿（主席权衡评审意见）、最高法院判案（法官校验律师主张）、英国议会听证（主席转述证人证词）
- 评测不依赖最终输出正确性，采用控制变量法：固定其他输入，仅修改子Agent输出的某一属性（如将多数评审意见替换为模板化无效内容、在律师意见中植入可核查错误、给证词附加限制条件），通过高层Agent输出的变化判断职责履行情况，评测结合规则校验与经人工标注校准的LLM评委。
### 关键实验
覆盖8款前沿闭源/开源LLM，共12000+Agent轮次测试，核心结果：1）仅2.9%的场景高层Agent会直接采纳子Agent植入的程序性错误；2）高层Agent跟随无意义模板化多数评审意见的比例最高达71%；3）转述证人证词时丢失标注限制条件的比例最高达65%；4）加入明确的角色义务prompt可降低15%-30%的失效率，但无法完全消除问题，且会改变控制组的行为。
### 核心结论
分层多Agent系统的可靠性不能仅靠端到端效果评估，也不能通过模型通用能力推断，必须针对高层角色的具体义务做专项行为测试。
