---
title: How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces
title_zh: 工具调用痕迹可泄露多少用户信息？Agent工具调用的隐私风险研究
authors:
- Donghang Duan
- Qingyu Liu
- Yifei Liu
- Na Zou
- Xia Hu
- Dongrui Liu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- University of Electronic Science and Technology of China
- The University of Sydney
arxiv_id: '2610.41885'
url: https://arxiv.org/abs/2610.41885
pdf_url: https://arxiv.org/pdf/2610.41885
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent安全 · 工具调用隐私泄露检测
tags:
- LLM Agent
- Privacy Leakage
- MCP
- Tool Call
- Benchmark
one_liner: 系统验证MCP工具调用痕迹的用户画像推断风险，开源含千份用户画像的PrivacyTrace评测基准
practical_value: '- 电商导购、生活服务类Agent可对MCP工具调用的参数、返回结果做最小化脱敏，比如模糊化用户预算、收货地址粒度，仅透传必要字段，降低用户消费能力、地域、健康状态等属性泄露风险

  - 对接第三方工具的推荐/Agent服务需避免跨会话、跨域的工具调用痕迹关联，给每个会话分配临时唯一标识路由请求，不使用持久用户ID，降低第三方基于痕迹构建用户长期画像的风险

  - 可借鉴合成用户+真实工具执行的评测范式，针对业务自有工具链做隐私风险自审计，无需真实用户数据即可评估泄露风险，降低合规评测成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent通过MCP协议对接外部工具已成为标准范式，工具调用痕迹（名称、参数、返回结果、调用序列）对第三方工具服务器天然可见，现有研究仅关注敏感数据直接泄露风险，未验证合法调用痕迹作为侧信道泄露用户长期属性的可能性，这一漏洞直接影响电商、服务类Agent的用户隐私合规性。

### 方法关键点
- 提出PrivacyTrace基准，融合官方人口统计数据与LLM一致性校验，生成1000份符合真实人口分布的合成用户画像，每份覆盖17个属性标签
- 覆盖旅行、健康、购物、职业学习4个领域，对接25个真实MCP工具服务器生成4000条Agent轨迹，共67950条工具调用记录
- 设计两类观察者威胁模型：仅能看到自身服务调用的本地服务器观察者、可跨会话跨域聚合全量痕迹的全局观察者，对比one-shot和两阶段攻击的画像推断效果

### 关键实验
用4款主流LLM作为攻击者，基线为仅用属性分布的先验猜测：单域工具痕迹下攻击成功率（ASR）从基线17.97%提升至26.25%；工具参数、返回结果是核心泄露源，分别比仅用元数据+调用序列的基线提升ASR 13.18、10.01个百分点；跨4域关联痕迹时ASR进一步提升到32.77%，但手机号、邮箱等精准标识符推断准确率极低。

**最值得记住的一句话：合法的MCP工具调用痕迹本身就是可被利用的用户画像侧信道，仅靠不直接传输敏感信息不足以保障Agent用户隐私。**
